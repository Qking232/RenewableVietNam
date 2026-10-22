import sys
sys.path.append(r'G:\My Drive\7. AI\Auto Post v2')
from super_productivity_tool import SuperProductivityClient

client = SuperProductivityClient()
task = client.get_task('Oi-5LhP4thHuCNQpNmoBy')
sub_ids = task.get('subTaskIds', [])
for sid in sub_ids:
    client.mark_done(sid, True)
    t = client.get_task(sid)
    print(f"Subtask {sid} ({t.get('title')}) marked DONE")
