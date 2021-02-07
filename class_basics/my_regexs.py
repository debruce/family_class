import re

line = input("What is your sentence? ")

m = re.search(r"[Tt]he\s+(\w+)\sbird\s+(\w+)", line)
if m:
    print("Got match")
    print(f"Match is first={m.group(1)} second={m.group(2)}")