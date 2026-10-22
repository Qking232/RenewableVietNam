import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
all_tasks = client.get_tasks()
active = [t for t in all_tasks if not t.get('isDone')]
print('Total active tasks across all projects:', len(active))
for a in active:
    print(f"[{a.get('projectId', 'No Project')}] [{a['id']}] {a.get('title')}")
