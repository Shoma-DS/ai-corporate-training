import { neon } from "@neondatabase/serverless";

const MAX_LIMIT = 2000;

function databaseUrl() {
  return process.env.DATABASE_URL || process.env.POSTGRES_URL || process.env.NEON_DATABASE_URL || "";
}

function getSql() {
  const url = databaseUrl();
  if (!url) {
    throw new Error("DATABASE_URL, POSTGRES_URL, or NEON_DATABASE_URL is required.");
  }
  return neon(url);
}

async function ensureSchema(sql) {
  await sql`
    CREATE TABLE IF NOT EXISTS prompt_timeline_events (
      repo_label text NOT NULL,
      event_id text NOT NULL,
      kind text NOT NULL DEFAULT '',
      source text NOT NULL DEFAULT '',
      actor text NOT NULL DEFAULT '',
      parent_id text NOT NULL DEFAULT '',
      event_timestamp timestamptz,
      timestamp_jst text NOT NULL DEFAULT '',
      prompt_original text NOT NULL DEFAULT '',
      prompt_preview text NOT NULL DEFAULT '',
      summary text NOT NULL DEFAULT '',
      actions jsonb NOT NULL DEFAULT '[]'::jsonb,
      tags jsonb NOT NULL DEFAULT '[]'::jsonb,
      meta jsonb NOT NULL DEFAULT '{}'::jsonb,
      event jsonb NOT NULL,
      created_at timestamptz NOT NULL DEFAULT now(),
      updated_at timestamptz NOT NULL DEFAULT now(),
      PRIMARY KEY (repo_label, event_id)
    )
  `;
  await sql`
    CREATE INDEX IF NOT EXISTS prompt_timeline_events_repo_timestamp_idx
      ON prompt_timeline_events (repo_label, event_timestamp, created_at)
  `;
}

function repoLabelFromRequest(req, body) {
  const fromQuery = typeof req.query.repo === "string" ? req.query.repo : "";
  const fromBody = body && typeof body.repo_label === "string" ? body.repo_label : "";
  const fromEnv = process.env.PROMPT_TIMELINE_REPO_LABEL || "";
  return (fromQuery || fromBody || fromEnv).trim();
}

function normalizeEvent(event, repoLabel) {
  const normalized = event && typeof event === "object" ? { ...event } : {};
  const eventId = String(normalized.id || "").trim();
  if (!eventId) return null;
  normalized.repo_label = repoLabel;
  normalized.actions = Array.isArray(normalized.actions) ? normalized.actions : [];
  normalized.tags = Array.isArray(normalized.tags) ? normalized.tags : [];
  normalized.meta = normalized.meta && typeof normalized.meta === "object" && !Array.isArray(normalized.meta)
    ? normalized.meta
    : {};
  return normalized;
}

function parseLimit(value) {
  const parsed = Number.parseInt(String(value || ""), 10);
  if (!Number.isFinite(parsed) || parsed <= 0) return MAX_LIMIT;
  return Math.min(parsed, MAX_LIMIT);
}

function bearerToken(req) {
  const header = req.headers.authorization || "";
  const match = /^Bearer\s+(.+)$/i.exec(header);
  return match ? match[1] : "";
}

function requestBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  if (typeof req.body !== "string" || !req.body.trim()) return {};
  try {
    const parsed = JSON.parse(req.body);
    return parsed && typeof parsed === "object" ? parsed : {};
  } catch {
    return {};
  }
}

async function readEvents(req, res) {
  const repoLabel = repoLabelFromRequest(req, null);
  if (!repoLabel) {
    res.status(400).json({ error: "repo query parameter is required" });
    return;
  }
  const sql = getSql();
  await ensureSchema(sql);
  const limit = parseLimit(req.query.limit);
  const rows = await sql`
    SELECT event
    FROM prompt_timeline_events
    WHERE repo_label = ${repoLabel}
    ORDER BY event_timestamp ASC NULLS LAST, created_at ASC
    LIMIT ${limit}
  `;
  res.setHeader("Cache-Control", "s-maxage=30, stale-while-revalidate=300");
  res.status(200).json({
    repo_label: repoLabel,
    source: "neon",
    events: rows.map((row) => row.event),
  });
}

async function writeEvents(req, res) {
  const expectedToken = process.env.PROMPT_TIMELINE_INGEST_TOKEN || "";
  if (!expectedToken || bearerToken(req) !== expectedToken) {
    res.status(401).json({ error: "Unauthorized" });
    return;
  }
  const body = requestBody(req);
  const repoLabel = repoLabelFromRequest(req, body);
  if (!repoLabel) {
    res.status(400).json({ error: "repo_label is required" });
    return;
  }
  const rawEvents = Array.isArray(body.events) ? body.events : [body.event].filter(Boolean);
  const events = rawEvents.map((event) => normalizeEvent(event, repoLabel)).filter(Boolean);
  if (!events.length) {
    res.status(400).json({ error: "events are required" });
    return;
  }

  const sql = getSql();
  await ensureSchema(sql);
  for (const event of events) {
    await sql`
      INSERT INTO prompt_timeline_events (
        repo_label,
        event_id,
        kind,
        source,
        actor,
        parent_id,
        event_timestamp,
        timestamp_jst,
        prompt_original,
        prompt_preview,
        summary,
        actions,
        tags,
        meta,
        event,
        updated_at
      )
      VALUES (
        ${repoLabel},
        ${event.id},
        ${String(event.kind || "")},
        ${String(event.source || "")},
        ${String(event.actor || "")},
        ${String(event.parent_id || "")},
        ${event.timestamp || null},
        ${String(event.timestamp_jst || "")},
        ${String(event.prompt_original || "")},
        ${String(event.prompt_preview || "")},
        ${String(event.summary || "")},
        ${JSON.stringify(event.actions)}::jsonb,
        ${JSON.stringify(event.tags)}::jsonb,
        ${JSON.stringify(event.meta)}::jsonb,
        ${JSON.stringify(event)}::jsonb,
        now()
      )
      ON CONFLICT (repo_label, event_id) DO UPDATE SET
        kind = EXCLUDED.kind,
        source = EXCLUDED.source,
        actor = EXCLUDED.actor,
        parent_id = EXCLUDED.parent_id,
        event_timestamp = EXCLUDED.event_timestamp,
        timestamp_jst = EXCLUDED.timestamp_jst,
        prompt_original = EXCLUDED.prompt_original,
        prompt_preview = EXCLUDED.prompt_preview,
        summary = EXCLUDED.summary,
        actions = EXCLUDED.actions,
        tags = EXCLUDED.tags,
        meta = EXCLUDED.meta,
        event = EXCLUDED.event,
        updated_at = now()
    `;
  }
  res.status(200).json({ repo_label: repoLabel, upserted: events.length });
}

export default async function handler(req, res) {
  if (req.method === "OPTIONS") {
    res.setHeader("Allow", "GET,POST,OPTIONS");
    res.status(204).end();
    return;
  }
  try {
    if (req.method === "GET") {
      await readEvents(req, res);
      return;
    }
    if (req.method === "POST") {
      await writeEvents(req, res);
      return;
    }
    res.setHeader("Allow", "GET,POST,OPTIONS");
    res.status(405).json({ error: "Method not allowed" });
  } catch (error) {
    res.status(500).json({ error: error instanceof Error ? error.message : "Unexpected error" });
  }
}
