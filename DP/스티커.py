# [B_S1] 스티커
# https://www.acmicpc.net/problem/9465
'''
테스트 케이스 개수 T가 주어지고, 
2n개의 스티커 종이의 2n (1 <= n <= 100,000)개의 점수가 주어진다.
각 스티커와 변을 공유하는 스티커는 사용할 수 없다고 할 때,
두 변을 공유하지 않는 스티커 점수의 최댓값?
* 시간 제한 1초
* 메모리 제한 256MB
'''

import sys

def input():
  return sys.stdin.readline()

t = int(input())
for _ in range(t):
  n = int(input())
  stickers = [list(map(int, input().split())) for _ in range(2)]

  dp = stickers.copy()          # dp[i][j] : stickers[i][j]를 포함하는 경우의 두 변을 공유하지 않는 스티커 점수의 최댓값
  for i in range(1 , n):
    dp[0][i] += max(dp[1][i - 1], dp[1][i - 2] if i - 2 >= 0 else 0)
    dp[1][i] += max(dp[0][i - 1], dp[0][i - 2] if i - 2 >= 0 else 0)
    
  print(max(max(dp[0]), max(dp[1])))
