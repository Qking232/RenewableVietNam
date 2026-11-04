with open('RenewableVietNam/invm/index_Rev.037.html', 'r', encoding='utf-8') as f:
    text = f.read()

colors = [
    (1, 'blue'),
    (2, 'sky'),
    (3, 'orange'),
    (4, 'emerald'),
    (5, 'teal'),
    (6, 'indigo')
]

for num, c in colors:
    old_str = f"""<div onclick="filterByPhaseAndSwitch('Giai đoạn {num}')" class="p-3.5 rounded-xl border border-slate-200 hover:border-{c}-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">"""
    new_str = f"""<div onclick="filterByPhaseAndSwitch('Giai đoạn {num}')" class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-700/80 hover:border-{c}-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 dark:bg-slate-800/80 hover:bg-white dark:hover:bg-slate-750 group">"""
    if old_str in text:
        text = text.replace(old_str, new_str)
        print(f"Replaced Stage {num}")
    else:
        print(f"Warning: Stage {num} not found")

with open('RenewableVietNam/invm/index_Rev.037.html', 'w', encoding='utf-8') as f:
    f.write(text)

