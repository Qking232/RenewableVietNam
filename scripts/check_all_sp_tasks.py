import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
projects = {p['id']: p['title'] for p in client.get_projects()}
print('Available projects:', projects)

all_tasks = client.get_tasks(include_done=False)
print(f'Total active tasks across all projects: {len(all_tasks)}')
for t in all_tasks:
    proj_title = projects.get(t.get('projectId'), 'Inbox/No Project')
    print(f"[{proj_title}] [{t['id']}] Parent={t.get('parentId')} | Title: {t.get('title')}")
