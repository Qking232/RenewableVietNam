import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
projects = {p['id']: p['title'] for p in client.get_projects()}
print('Projects:', projects)

tasks = client.get_tasks(include_done=True)
print(f'Total tasks retrieved: {len(tasks)}')

active_tasks = [t for t in tasks if not t.get('isDone')]
print(f'Active tasks: {len(active_tasks)}')
for t in active_tasks:
    p_name = projects.get(t.get('projectId'), 'Unknown/Inbox')
    print(f"ACTIVE: [{t['id']}] Proj={p_name} | Parent={t.get('parentId')} | Title={t.get('title')}")

print("\nLast 10 tasks in list:")
for t in tasks[-10:]:
    p_name = projects.get(t.get('projectId'), 'Unknown/Inbox')
    print(f"[{t['id']}] Done={t.get('isDone')} | Proj={p_name} | Title={t.get('title')}")
