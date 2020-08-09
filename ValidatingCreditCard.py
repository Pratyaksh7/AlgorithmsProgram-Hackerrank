import re

n = int(input())
arr = [input() for i in range(n)]
# expression for 16 digits number
pattern = re.compile(r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$")
# expression for 4 consecutive same numbers
pattern2 = re.compile(r"([\d])\1\1\1")
for i in arr:
    if re.match(pattern, i) and not re.search(pattern2, i.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
