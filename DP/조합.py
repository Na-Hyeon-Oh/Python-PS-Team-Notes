# [B_S3] 조합
# https://www.acmicpc.net/problem/2407
'''
nCm (5 <= n <= 100, 5 <= m <= 100, m <= n)
* 시간 제한 2초
* 메모리 제한 128MB
'''

# ***

import itertools

n, m = map(int, input().split())
result = itertools.combinations(range(1, n + 1), m)
print(len(list(result)))

'''
* n이 커질 수록 시간초과/메모리초과
'''


# i.
from math import factorial

n, m = map(int, input().split())

up = factorial(n)
down = factorial(n - m) * factorial(m)
print(up // down)

# ii.

n, m = map(int, input().split())

min = min(m, n - m)
dp = [1] * (n + 1)                # dp[i] = nCi
for i in range(1, min + 1):
  dp[i] = dp[i - 1] * (n + 1 - i) // i

print(dp[min])

'''
* int(), //의 연산이 다르게 
'''

# iii.

import sys
n , m = map(int, sys.stdin.readline().split(" "))
dp = [[0 for i in range(101)] for j in range(101)]
for i in range(1,101):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2,101):
    for t in range(1,i):
        dp[i][t] = dp[i-1][t-1] + dp[i-1][t]
print(dp[n][m])

'''
https://ddggblog.tistory.com/133
'''

