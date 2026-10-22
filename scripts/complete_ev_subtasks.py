import sys
sys.path.append(r'G:\My Drive\7. AI\Auto Post v2')
from super_productivity_tool import SuperProductivityClient

client = SuperProductivityClient()
task = client.get_task('mBrwjUuXZvsqjqvQdup-T')
for sid in task.get('subTaskIds', []):
    client.mark_done(sid, True)
    t = client.get_task(sid)
    print(f"Subtask {sid} ({t.get('title')}) marked DONE")
