# 트리 순회
# https://www.acmicpc.net/problem/22856
'''
노드가 N개인 이진 트리가 있을 때, 유사 중위 순회를 할 때, 이동 횟수를 구하시오.
유사 중위 순회는 루트 노드에서 시작하며, 다음과 같이 진행된다.
1. 현재 위치한 노드(a)의 왼쪽 자식 노드(b)가 존재하고 아직 방문하지 않았다면, 왼쪽 자식 노드로 이동한다.
2. 그렇지 않고 현재 위치한 노드의 오른쪽 자식 노드(c)가 존재하고 아직 방문하지 않았다면, 오른쪽 자식 노드로 이동한다.
3. 그렇지 않고 현재 노드가 유사 중위 순회의 끝이라면(b, c = -1), 유사 중위 순회를 종료한다.
4. 그렇지 않고 부모 노드가 존재한다면, 부모 노드로 이동한다.
5. 유사 중위 순회를 종료할 때까지 1~4를 반복한다.
* 1 <= N <= 100,000, 1 <= a, b <= N
* 제한 시간 1초
'''

import sys
sys.setrecursionlimit(10**6)

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
parentNodes = [0] * (n + 1)      # node id가 1부터 시작하므로
leftChild = dict()
rightChild = dict()
for _ in range(n):
  a, b, c = map(int, input().split())
  if b != -1: parentNodes[b] = a
  if c != -1: parentNodes[c] = a
  leftChild[a] = b
  rightChild[a] = c
    
lastNode = 0
def traverse(node):
  global lastNode
  if node == -1: return
  traverse(leftChild[node])  
  lastNode = node
  traverse(rightChild[node]) 

traverse(1)
lines = 2 * (n - 1)
depthFromLastNode = 0
while lastNode != 1:
  depthFromLastNode += 1
  lastNode = parentNodes[lastNode]
print(lines - depthFromLastNode)

'''
- 재귀 활용 문제
- 중위 순회 후 마지막 node 찾고, 전체 간선 개수의 두 배에서 마지막에 방문하는 노드를 지나온 간선의 개수 빼주기
- 재귀 안에서 매번 for문으로 node의 parent와 child를 탐색하기에는 시간 
'''
