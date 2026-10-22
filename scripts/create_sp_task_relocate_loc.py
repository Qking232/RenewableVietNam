import sys
sys.path.append(r'G:\My Drive\7. AI\Auto Post v2')
from super_productivity_tool import SuperProductivityClient

client = SuperProductivityClient()
task = client.create_task(
    title='Relocate "My Location" to Dedicated Floating Bottom-Right Map Control Icon (Icon-Only, Zero Text)',
    project_id='erVuLc3imEXbqnx6flEC9',
    notes='Move "My Location" from the quick chips row to the bottom right side of the map as an icon-only circular floating action button (Google Maps style). Remove text label.'
)
if task:
    print(f"CREATED_TASK_ID:{task.get('id')}")
else:
    print("FAILED_TO_CREATE")
