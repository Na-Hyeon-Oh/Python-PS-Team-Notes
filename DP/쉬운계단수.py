# [B_S1] 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
'''
길이가 N(1 <= N <= 100)인 계단수의 개수를 1,000,000,000으로 나눈 나머지 출력
* 계단수: 인접한 모든 자리의 차이가 1인 수   ex. 12345
* 시간 제한 1초
* 메모리 제한 256MB
'''

import sys

def input():
  return sys.stdin.readline()

n = int(input())

dp = [[0 for j in range(10)] for i in range(n)]              # dp[i][j]: i 길이의 수에서 앞에오는 숫자의 개수
for i in range(1, 10):
  dp[0][i] = 1
for i in range(1, n):
  for j in range(10):
    target = dp[i - 1][j]
    if j < 9: dp[i][j + 1] += target
    if j > 0: dp[i][j - 1] += target

result = 0
for i in range(10):
  result += dp[n - 1][i]
print(result % 1000000000)

'''
- 뒤의 가능한 수를 결정하는 건 앞의 수
- 모든 수를 리스트에 저장하기 보다 배열의 인덱스로서 표시 (0~9)
'''
