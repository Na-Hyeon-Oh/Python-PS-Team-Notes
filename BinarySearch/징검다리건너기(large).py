# 징검다리 건너기 (large)
# https://www.acmicpc.net/problem/22871
'''
N개의 돌이 일렬로 나열되어 있을 때 (A1A2...Ai...AN), 가장 왼쪽의 돌에서 출발하여 가장 오른쪽에 있는 돌로 다음과 같이 건너가려 한다.
1. 항상 오른쪽으로만 이동 가능하다.
2. i번째 돌에서 j번째 돌로 이동할 때 (j - i) * (1 + |Ai - Aj|)만큼 힘을 쓴다.
3. 돌을 한 번 건너갈 때마다 쓸 수 있는 힘은 최대 K이다.
가장 왼쪽 돌에서 가장 오른쪽의 돌로 건너갈 수 있는 모든 경우 중 K의 최솟값?
* 2 <= N <= 5,000, 1 <= Ai <= 1,000,000
* 제한 시간 2초
'''

# i. PyPy3

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

INF = 1e7
dp = [0] + [INF] * (n - 1)
for i in range(1, n):
  for j in range(i + 1, n + 1):
    dp[j - 1] = min(dp[j - 1], max(dp[i - 1], (j - i) * (1 + abs(a[i - 1] - a[j - 1]))))
    
print(dp[-1])


# ii. Python3

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
for j in range(1, n):
  maxK = []
  for i in range(0, j):
    maxK.append(max(dp[i], (j - i) * (1 + abs(a[i] - a[j]))))
  dp[j] = min(maxK)
    
print(dp[-1])


'''
- 매 번 돌다리를 건널 때마다 최소의 힘을 쓰는 것이 k의 최솟값
- dp에 각 지점까지의 최솟값 저장
'''
