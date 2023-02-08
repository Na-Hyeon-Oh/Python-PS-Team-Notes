# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
'''
루트 없는 트리가 주어진다.
트리의 루트를 1로 정했을 때 각 노드의 부모를 구하라.
* 2 <= N <= 100,000
* 제한 시간 1초
'''

import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

def dfs(start):
  if visited[start] != True:
    visited[start] = True
    for i in range(len(graph[start])):
      if visited[graph[start][i]] != True:
        child = graph[start][i]
        parents[child] = start
        dfs(child)
        
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

parents = dict()
visited = [False] * (n + 1)

dfs(1)
for i in range(2, n + 1):
  print(parents[i])

'''
node1부터 dfs를 수행하며 깊이를 탐색하는데, 방문하지 않은 노드일 경우 child이므로 해당 child에서 node의 parent를 dictionary로 저장
'''
