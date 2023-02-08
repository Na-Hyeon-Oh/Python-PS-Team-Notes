# 효율적인 해킹
# https://www.acmicpc.net/problem/1325
'''
N개의 컴퓨터로 이루어진 회사를 한 번의 해킹으로 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 (오름차순으로) 출력하라.
해당 회사의 컴퓨터는 신뢰하는 컴퓨터와 신뢰하지 않는 컴퓨터로 나누어져 있는데, A가 B를 신뢰하면 B는 A를 해킹할 수 있다.
* 자연수 : N <= 10,000, M <= 100,000
* 제한 시간 5초
'''

import sys
from collections import deque

def input():
  return sys.stdin.readline()

def bfs(start):
  visited = [False] * (n+1)
  visited[start] = True
  queue = deque([start])
  cnt = 1
  while queue:
    cur = queue.popleft()
    for connection in network[cur]:
      if visited[connection] != True:
        visited[connection] = True
        queue.append(connection)
        cnt += 1
  return cnt

n, m = map(int, input().split())
network = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  network[b].append(a)
        
maxCnt = 0
result = []
for i in range(1, n+1):
  cnt = bfs(i)
  if maxCnt == cnt: result.append(i)
  elif cnt > maxCnt:
    maxCnt = cnt
    result.clear()
    result.append(i)

print(*result)    

'''
- dfs/bfs를 모든 node마다 실행
- bfs : O(N+M)인데 모든 노드마다 하므로 O(N*M) -> 최악의 경우 10^9 연산
'''
