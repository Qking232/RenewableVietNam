import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
tasks = client.get_tasks('erVuLc3imEXbqnx6flEC9', include_done=True)
active_vibe = [t for t in tasks if not t.get('isDone')]
print(f'Active Vibe Coding tasks ({len(active_vibe)}):')
for t in active_vibe:
    print(f"ID: {t['id']}")
    print(f"Title: {t.get('title')}")
    print(f"ParentId: {t.get('parentId')}")
    print(f"SubtaskIds: {t.get('subTaskIds')}")
    print(f"Created: {t.get('created')}")
    print(f"Notes: {t.get('notes')}")
    print('-'*50)
