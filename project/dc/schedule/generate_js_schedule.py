#!/usr/bin/env python3
import json
import re
from datetime import datetime, timedelta

def add_workdays(curr_date: datetime, days: int) -> datetime:
    res = curr_date
    if days >= 0:
        added = 0
        while added < days:
            res += timedelta(days=1)
            if res.weekday() < 5:
                added += 1
    else:
        subtracted = 0
        while subtracted < abs(days):
            res -= timedelta(days=1)
            if res.weekday() < 5:
                subtracted += 1
    return res

# Read generate_datacenter_schedule_Rev.006.py
source_file = r"G:\My Drive\7. AI\DataCenter_Schedule\generate_datacenter_schedule_Rev.006.py"
with open(source_file, "r", encoding="utf-8") as f:
    code = f.read()

# Extract wbs_data
wbs_match = re.search(r"wbs_data = \[(.*?)\]\s+# 2\. Activity Definitions", code, re.DOTALL)
act_match = re.search(r"activities = \[(.*?)\]\s+# 3\. Logic Network Relationships", code, re.DOTALL)
rel_match = re.search(r"relationships = \[(.*?)\]\s+act_dict =", code, re.DOTALL)

scope = {
    "datetime": datetime,
    "timedelta": timedelta,
    "add_workdays": add_workdays,
    "proj_short_name": "DC36-T3",
    "proj_name": "Hyperscale Data Center Facility 36MW Tier III"
}
exec("wbs_data = [" + wbs_match.group(1) + "]", scope)
exec("activities = [" + act_match.group(1) + "]", scope)
exec("relationships = [" + rel_match.group(1) + "]", scope)

wbs_data = scope["wbs_data"]
activities = scope["activities"]
relationships = scope["relationships"]

start_anchor = datetime(2027, 1, 4, 8, 0)
act_dict = {a[1]: a for a in activities}
wbs_dict = {w[0]: w for w in wbs_data}

early_start = {}
early_finish = {}
preds = {a[1]: [] for a in activities}
succs = {a[1]: [] for a in activities}

for p, s, rel_type, lag in relationships:
    preds[s].append((p, rel_type, lag))
    succs[p].append((s, rel_type, lag))

in_degree = {a[1]: len(preds[a[1]]) for a in activities}
queue = [a[1] for a in activities if in_degree[a[1]] == 0]
top_order = []

while queue:
    u = queue.pop(0)
    top_order.append(u)
    for v, _, _ in succs[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

for code_id in top_order:
    act = act_dict[code_id]
    duration = act[4]
    if not preds[code_id]:
        es = start_anchor
    else:
        es = start_anchor
        for p, _, lag in preds[code_id]:
            pred_ef = early_finish[p]
            candidate_es = add_workdays(pred_ef, lag) if lag > 0 else pred_ef
            if candidate_es.hour >= 17:
                candidate_es = add_workdays(candidate_es, 1).replace(hour=8, minute=0)
            if candidate_es > es:
                es = candidate_es
    ef = add_workdays(es, duration) if duration > 0 else es
    early_start[code_id] = es
    early_finish[code_id] = ef

project_finish = max(early_finish.values())

late_finish = {}
late_start = {}
for code_id in reversed(top_order):
    act = act_dict[code_id]
    duration = act[4]
    if not succs[code_id]:
        lf = project_finish
    else:
        lf = datetime(2099, 1, 1)
        for s, _, lag in succs[code_id]:
            succ_ls = late_start[s]
            candidate_lf = succ_ls
            if candidate_lf < lf:
                lf = candidate_lf
    ls = add_workdays(lf, -duration) if duration > 0 else lf
    late_start[code_id] = ls
    late_finish[code_id] = lf

total_float_days = {}
for code_id in top_order:
    cur = early_finish[code_id]
    target = late_finish[code_id]
    diff = 0
    if target > cur:
        temp = cur
        while temp < target:
            temp += timedelta(days=1)
            if temp.weekday() < 5:
                diff += 1
    total_float_days[code_id] = diff

# Helper to map task to 3D phase & element tag
def get_phase_and_tag(act_code, wbs_id):
    if wbs_id in ("110", "120", "130"):
        return 1, "pm_eng"
    elif wbs_id == "141": # Substructure
        if act_code in ("A4110",):
            return 1, "excavation"
        elif act_code in ("A4120", "A4130"):
            return 1, "piling"
        elif act_code in ("A4140", "A4150"):
            return 2, "raft_slab"
        return 2, "substructure"
    elif wbs_id == "142": # Superstructure
        if act_code in ("A4210",):
            return 2, "plinths_columns_g"
        elif act_code in ("A4220",):
            return 3, "slab_l1"
        elif act_code in ("A4230", "A4250"):
            return 3, "slab_l2_shear"
        elif act_code in ("A4240",):
            return 4, "steel_roof_gantry"
        return 3, "superstructure"
    elif wbs_id == "143": # Envelope
        if act_code in ("A4310",):
            return 4, "facade_panels"
        elif act_code in ("A4320", "A4330"):
            return 4, "roof_membrane"
        elif act_code in ("A4340", "M4350"):
            return 4, "envelope_doors"
        return 4, "envelope"
    elif wbs_id == "151": # Substation
        return 5, "substation"
    elif wbs_id == "152": # Generator farm
        return 5, "generators"
    elif wbs_id == "153": # Chilled water plant
        if act_code in ("A5330",):
            return 5, "cooling_towers"
        return 5, "chillers"
    elif wbs_id == "154": # White Space
        if act_code in ("A5430",):
            return 6, "raised_floor"
        elif act_code in ("A5440",):
            return 6, "overhead_busways"
        elif act_code in ("A5450", "A5460"):
            return 6, "crah_units"
        elif act_code in ("A5470",):
            return 6, "server_racks_hac"
        elif act_code in ("A5410", "A5420"):
            return 6, "ups_batteries"
        return 6, "white_space"
    elif wbs_id == "155": # BMS, EPMS, Fire
        return 6, "bms_fire"
    elif wbs_id in ("161", "162"):
        return 7, "cx_static"
    elif wbs_id in ("163",):
        return 7, "cx_dynamic"
    elif wbs_id in ("164",):
        return 7, "cx_load_banks"
    elif wbs_id == "170":
        return 8, "cod_operational"
    return 1, "general"

activities_export = []
for code_id in top_order:
    act = act_dict[code_id]
    w_info = wbs_dict.get(act[3], (act[3], "", "", act[3], act[3]))
    es = early_start[code_id]
    ef = early_finish[code_id]
    ls = late_start[code_id]
    lf = late_finish[code_id]
    tf = total_float_days[code_id]
    phase, tag = get_phase_and_tag(code_id, act[3])
    
    activities_export.append({
        "id": act[0],
        "code": code_id,
        "name": act[2],
        "wbs_id": act[3],
        "wbs_code": w_info[3],
        "wbs_name": w_info[4],
        "duration": act[4],
        "type": act[5],
        "start": es.strftime("%Y-%m-%d"),
        "finish": ef.strftime("%Y-%m-%d"),
        "startTimestamp": int(es.timestamp() * 1000),
        "finishTimestamp": int(ef.timestamp() * 1000),
        "late_start": ls.strftime("%Y-%m-%d"),
        "late_finish": lf.strftime("%Y-%m-%d"),
        "total_float": tf,
        "is_critical": (tf == 0),
        "phase": phase,
        "tag": tag,
        "predecessors": [p[0] for p in preds[code_id]],
        "successors": [s[0] for s in succs[code_id]]
    })

wbs_export = [
    {
        "id": w[0],
        "parent_id": w[1],
        "code": w[3],
        "name": w[4]
    } for w in wbs_data
]

milestones_export = [
    a for a in activities_export if a["type"] in ("TT_Mile", "TT_FinMile")
]

min_ts = min(a["startTimestamp"] for a in activities_export)
max_ts = max(a["finishTimestamp"] for a in activities_export)

js_content = f"""// Institutional DC36-T3 Hyperscale Datacenter Schedule Dataset
// Oracle Primavera P6 Relational Schema / DCMA-14 Standard Compliance

window.DC36_SCHEDULE = {{
    project_id: "DC36-T3",
    project_name: "Hyperscale Data Center Facility 36MW Tier III",
    min_date: "{datetime.fromtimestamp(min_ts/1000).strftime('%Y-%m-%d')}",
    max_date: "{datetime.fromtimestamp(max_ts/1000).strftime('%Y-%m-%d')}",
    min_timestamp: {min_ts},
    max_timestamp: {max_ts},
    total_calendar_days: {int((max_ts - min_ts) / (1000 * 3600 * 24))},
    total_activities: {len(activities_export)},
    wbs_hierarchy: {json.dumps(wbs_export, indent=2)},
    milestones: {json.dumps(milestones_export, indent=2)},
    activities: {json.dumps(activities_export, indent=2)},
    
    // Phase metadata
    phases: [
        {{ id: 1, name: "Site Clearing, Bulk Excavation & Piling", start_date: "2027-01-04", finish_date: "2027-07-30", target_mw: 0 }},
        {{ id: 2, name: "Substructure Raft Slab & Ground Plinths", start_date: "2027-08-02", finish_date: "2027-11-26", target_mw: 0 }},
        {{ id: 3, name: "Concrete Superstructure (L1 & L2 Slabs)", start_date: "2027-11-29", finish_date: "2028-03-10", target_mw: 0 }},
        {{ id: 4, name: "Steel Roof Trusses & Precast Facade Envelope", start_date: "2028-02-07", finish_date: "2028-07-17", target_mw: 0 }},
        {{ id: 5, name: "Heavy MEP (110kV Substation, 16 Gensets, 6 Chillers)", start_date: "2028-07-17", finish_date: "2028-12-08", target_mw: 0 }},
        {{ id: 6, name: "White Space Fit-Out (Halls 1-4, Busways, CRAH & Racks)", start_date: "2028-07-17", finish_date: "2029-01-15", target_mw: 0 }},
        {{ id: 7, name: "Testing & Commissioning (Cx L1-L5, 36MW Heat Soak)", start_date: "2029-01-15", finish_date: "2029-07-23", target_mw: 36 }},
        {{ id: 8, name: "Commercial Operation Date (COD) & Hyperscale Live", start_date: "2029-07-23", finish_date: "2029-10-01", target_mw: 36 }}
    ]
}};
"""

output_path = r"G:\My Drive\7. AI\DataCenter_3D_Evolution\js\datacenter_schedule.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {output_path} with {len(activities_export)} activities.")
