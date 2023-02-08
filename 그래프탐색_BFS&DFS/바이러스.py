# 바이러스
# https://www.acmicpc.net/problem/2606
'''
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸린다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라.
* 컴퓨터 수 <= 100, 각 컴퓨터에는 1번부터 차례대로 번호가 메겨진다.
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
network = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
  connection = list(map(int, input().split()))
  network[connection[0]].append(connection[1])
  network[connection[1]].append(connection[0])

result = 0
status = [False for _ in range(n + 1)]        # 0: unvisited, 1: visited(Virus)
def dfs(start):
  global result
  if status[start] != True:
    status[start] = True
    for i in range(len(network[start])):
      if status[network[start][i]] != True:
        dfs(network[start][i])
        result += 1

dfs(1)
print(result)

'''
- DFS 사용: 방향이 없기 때문에 network에 양쪽의 노드에 모두 connection을 표시해야 한다.
'''
