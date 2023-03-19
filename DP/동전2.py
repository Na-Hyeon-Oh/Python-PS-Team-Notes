# [B_G5] 동전 2
# https://www.acmicpc.net/problem/2294
'''
n(1 <= n <= 100)가지 동전이 있을 때, 그 가치(<= 100,000)의 합이 k(1 <= k <= 10,000)원이 되도록 하려 한다.
동전의 개수의 최솟값?
* 시간 제한 1초
* 메모리 제한 128MB
'''

import sys

def input():
  return sys.stdin.readline()

n, k = map(int, input().split())
coin = []
dp = [1e7] * (k + 1)            # dp[i]: 가치의 합이 i원일 때 최소 동전 개수
for _ in range(n):
  ci = int(input())
  if ci <= k: 
    coin.append(ci)
    dp[ci] = 1

for value in coin:
  for i in range(value + 1, k + 1):
     dp[i] = min(dp[i - value] + 1, dp[i])          # 동전 개수 하나 더한 값과 기존 값 비교 후 최솟값 

if dp[k] != 1e7: print(dp[k])
else: print(-1)                  # k인 경우를 만들 수 없을 때

  
