import os

base = '講座'
courses = sorted(os.listdir(base))
total_missing = 0
for course in courses:
    cpath = os.path.join(base, course)
    if not os.path.isdir(cpath):
        continue
    sessions = sorted([d for d in os.listdir(cpath) if d[:2].isdigit()])
    if not sessions:
        continue
    print(f'=== {course} ===')
    for s in sessions:
        imgdir = os.path.join(cpath, s, 'スライド画像')
        if os.path.isdir(imgdir):
            count = len([f for f in os.listdir(imgdir) if f.lower().endswith('.png')])
        else:
            count = 0
        missing = max(0, 40 - count)
        total_missing += missing
        marker = 'OK' if count >= 40 else f'missing {missing}'
        print(f'  {s}: {count}枚 ({marker})')
print()
print(f'TOTAL MISSING (approx, assuming 40/session): {total_missing}')
