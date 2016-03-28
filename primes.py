import pandas as pd
data = pd.read_csv('primes-to-100k.txt', encoding='utf-8')
prime = data['prime']
lst = []
for i in range(9592):
    lst.append(prime[i])
print(lst)
