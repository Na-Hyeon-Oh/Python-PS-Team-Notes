'''
* 다시 풀어보기 
# L2. 전력망을 둘로 나누기
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있을 때,
이 전선들 중 하나를 끊어 전력망 네트워크를 2개로 분할하려 한다.
이 때 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추려고 할 때, 그 개수의 차이 최솟값을 출력하시오.
입력으로는 전선[v1, v2] 정보가 주어진다.
'''


from collections import deque

global graph
graph = []

def solution(n, wires):
    global graph
    graph = [[] for _ in range(n)]
    for [x, y] in wires:
        graph[x - 1].append(y)
        graph[y - 1].append(x)
    
    answer = 1e3
    for [x, y] in wires:
        answer = min(abs(connection(n, x, y) - connection(n, y, x)), answer)
    return answer

def connection(n, startNode, notConnectedNode):
    connection = [startNode]
    queue = deque()
    visited = [False] * n
    visited[notConnectedNode - 1] = True
    queue.append(startNode)
    while queue:
        i = queue.popleft()
        if visited[i - 1]: continue
        visited[i - 1] = True
        connection.append(i)
        queue.extend(graph[i - 1])
    return len(connection)
  
  
 '''
특정 연결을 끊었을 때, 각 node에서 이어질 수 있는 node의 개수를 bfs로 구하는 알고리즘
- 이를 위해 사전에 각 node에 연결된 node를 graph에 저장해두었다
'''
