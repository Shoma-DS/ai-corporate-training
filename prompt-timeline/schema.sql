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
);

CREATE INDEX IF NOT EXISTS prompt_timeline_events_repo_timestamp_idx
  ON prompt_timeline_events (repo_label, event_timestamp, created_at);
