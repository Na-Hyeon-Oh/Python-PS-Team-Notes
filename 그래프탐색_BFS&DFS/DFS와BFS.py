# DFS와 BFS
# https://www.acmicpc.net/problem/1260
'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하라.
방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문한다.
* 1 <= N(정점 개수) <= 1,000, 1 <= M(간선 개수) <= 10,000
* 제한 시간 2초
'''

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

def dfs(start):
  if dfsVisited[start] != True:
    dfsVisited[start] = True
    print(start, end=' ')
    for i in range(len(graph[start])):
      dfs(graph[start][i])

def bfs(start):
  queue = deque([start])
  while queue:
    node = queue.popleft()
    bfsVisited[node] = True
    print(node, end=' ')
    for connection in graph[node]:
      if bfsVisited[connection] != True:
        queue.append(connection)
        bfsVisited[connection] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)
for connection in graph:
  connection.sort()

dfsVisited = [False] * (n + 1)
bfsVisited = [False] * (n + 1)

dfs(v)
print()
bfs(v)

'''

'''
