# [B_S1] 포도주 시식
# https://www.acmicpc.net/problem/2156
'''
다음의 규칙으로 포도주를 맛볼 때, 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램?
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
* 1 <= n (포도주 잔의 개수) <= 10,000
* 시간 제한 2초
* 메모리 제한 128MB
'''

import sys

def input():
  return sys.stdin.readline()

n = int(input())
liquids = [int(input()) for _ in range(n)]

dp = [0] * n          # dp[i]: liquids[i]까지의 최대 포도주 양
dp[0] = liquids[0]
for i in range(1, n):
  dp[i] = max(liquids[i] + (dp[i - 2] if i >= 2 else 0), liquids[i] + (liquids[i - 1] + (dp[i - 3] if i >= 3 else 0)), dp[i - 1])

print(max(dp))

'''
i. dp[i]가 liquids[i]를 포함하는 경우
  (i) liquids[i - 1]가 포함된 경우
  (ii) liquids[i - 2]가 포함된 경우
ii. dp[i]가 liquids[i]를 포함하지 않는 경우
'''
