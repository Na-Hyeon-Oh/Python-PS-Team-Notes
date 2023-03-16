# [B_S1] 징검다리 건너기 (small)
# https://www.acmicpc.net/problem/22869
'''
N개의 돌이 일렬로 나열되어 있고 각 돌에는 Ai의 수가 부여되어 있다.
가장 왼쪽에 있는 돌에서 출발하여 가장 오른쪽의 돌로 건너가려 할 때 다음의 규칙을 따른다.
1. 항상 오른쪽으로만 이동 가능
2. i번째 돌에서 j(i<j)번째 돌로 이동할 때, (j - i) * (1 + |Ai - Aj|)만큼 힘이 듦
3. 돌을 한 번 건널 때 쓸 수 있는 힘은 최대 K
이 때 가능 여부를 출력하라.
* 2 <= N(돌의 개수) <= 5,000, 1 <= K (최대 힘) <= 1,000, 1 <= Ai <= 1,000
* 시간 제한 1초
* 메모리 제한 1024MB
'''

import sys

def input():
  return sys.stdin.readline()

n, k = map(int, input().split())
a = list(map(int, input().split()))

MAX = 1e8
dp = [MAX] * n            # dp[i]: i번째 돌에 닿기 위한 최소 에너지
dp[0] = 0
for i in range(n):
  if dp[i] != MAX:
    for j in range(i + 1, n):
      energy = (j - i) * (1 + abs(a[i] - a[j]))
      dp[j] = min(dp[j], (energy if energy <= k else MAX))

if dp[-1] <= k: print("YES")
else: print("NO")


'''
PyPy3
- 각 돌의 위치에서 오른쪽에 위치한 돌까지의 에너지가 k보다 크지 확인 -> 최악 O(N^2)
'''
