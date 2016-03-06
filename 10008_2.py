import re
from collections import Counter

n = int(input())
line = []
for i in range(n):
    line += re.findall('[a-zA-Z]', input().strip())
c = Counter(c.upper() for c in line)
for k, v in c.most_common():
    print(k, v)
