# [B_G5] 퇴사 2
# https://www.acmicpc.net/problem/15486
'''
N + 1일째 되는 날 퇴사를 할 때, 남은 N(1<= N <= 1,500,000)일동안 최대한 많은 상담을 하려 한다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti(1 <= Ti <= 50)와 상담을 했을 때 받을 수 있는 금액 Pi(1 <= Pi <= 1,000)로 이루어져 있다.
얻을 수 있는 최대 이익?
* 시간 제한 2초
* 메모리 제한 512MB
'''

import sys

def input():
  return sys.stdin.readline()

n = int(input())
t = []
p = []
for _ in range(n):
  ti, pi = map(int, input().split())
  t.append(ti)
  p.append(pi)

dp = [0] * (n + 1)                    # dp[i]: 뒤에서 i까지의 최댓값
for i in range(n):
  idx  = n - i
  dp[idx] = max((p[idx - 1] if t[idx - 1] <= i + 1 else 0) + (dp[idx + t[idx - 1]] if idx + t[idx - 1] <= n else 0), dp[idx + 1] if idx + 1 <= n else 0)

print(dp[1])

'''
- dp[n]을 만들어 각 원소는 i~n까지의 최대 이익 저장
- dp[i]에 최대 이익을 저장하기 위해, p[i]를 포함하는 경우와 p[i]가 포함되지 않는 경우를 나눠서 생각하면, 선자는 t[i]를 고려하여 dp[i + t[i]]를 p[i]에 더해준 값이고, 후자는 이전에 구한 값인 dp[i + 1]
'''
