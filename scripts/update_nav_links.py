import os

index_file = r"G:\My Drive\7. AI\RenewableVietNam\index.html"
with open(index_file, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace('href="/projectenergy/"', 'href="https://wind.renewablevietnam.com/"')
c = c.replace('href="/evcharging/"', 'href="https://ev.renewablevietnam.com/"')
c = c.replace('href="/hub/"', 'href="https://legal.renewablevietnam.com/"')

with open(index_file, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated index.html links successfully")
