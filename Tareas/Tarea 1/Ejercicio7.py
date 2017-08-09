#-*- coding:utf-8 -*-
n = 111000
criba = [True] * n

for i in range(2, int(n ** .5) + 1):
    for j in range(i * i, n + 1, i):
        criba[j - 1] = False
primos = [p for p in range(2, len(criba) + 1) if criba[p - 1]]
print primos[10000]
