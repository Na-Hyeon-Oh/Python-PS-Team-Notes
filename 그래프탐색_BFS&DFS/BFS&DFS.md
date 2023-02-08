# 그래프 탐색 알고리즘 : BFS / DFS

## PreRequisites

### 자료구조

#### Stack

- LIFO(Last In First Out); 후입선출

##### Stack in Python

list 활용

```
 stack = []
 
 stack.append(5)          # 삽입
 stack.append(2)
 stack.pop()              # 삭제
 
 print(stack[::-1])       # 최상단 원소부터 출력
 print(stack)             # 최하단 원소부터 출력
```
 
#### Queue
 
- FIFO(First In First Out); 선입선출
 
##### Queue in Python
 
deque library를 활용

- list를 사용할 수 있지만 연산에 있어 시간 복잡도가 높아짐

```
from collections import deque

queue = deque()

queue.append(5)           # 삽입
queue.append(2)       
queue.popleft()           # 삭제    # O(1) 

print(queue)              # 먼저 들어온 순서대로 출력
print(queue.reverse())    # 나중에 들어온 원소부터 출력
```

### 재귀 함수

자기 자신을 다시 호출하는 함수

- 종료 조건 명시하여야 함수가 무한히 호출되지 않음

- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓이는데, 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

##### 재귀 함수 In Python

내부적으로 recursion depth가 정해져 있다.

Ex1. 팩토리얼

```
def factorial(n):
  if n <= 1: return 1
  return n * factorial(n - 1)
```

Ex2. 최대공약수 계산(유클리드 호제법)

- 두 자연수 A, B에 대하여 A를 B로 나눈 나머지를 R이라고 할 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

```
def gcd(a, b):
  if a % b == 0: return b
  else: return gcd(b, a % b)
```


## DFS (Depth-First Search; 깊이 우선 탐색)

깊은 부분을 우선적으로 탐색하는 알고리즘

- 스택 자료구조 (혹은 재귀 함수)를 다음과 같이 이용한다.

  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다.
      방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  4. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

 ex. 재귀함수 사용
 
 ```
 # 각 노드의 연결 정보 표현
 graph = [
  [], 
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
 ]
 
 # 각 노드의 방문 정보 표현
 visited = [False] * 9
 
 def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
   if not visited[i]: dfs(graph, i, visited)
  
dfs(graph, 1, visited)

 ```


## BFS (Breadth-First Search; 너비 우선 탐색)

그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘

- 큐 자료구조를 다음과 같이 이용한다.
  
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

- 전체 노드의 탐색 순서 (큐에 들어가는 순서)가 동일한 노드가 먼저 들어가므로 특정 조건에서의 최단 경로 문제 등에 활용됨

ex.
```
from collections import deque

 # 각 노드의 연결 정보 표현
 graph = [
  [], 
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
 ]
 
 # 각 노드의 방문 정보 표현
 visited = [False] * 9
 
 def bfs(graph, start, visited):
  # queue를 위해 deque 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
   # 큐에서 하나의 원소를 뽑아 출력하기
   v = queue.popleft()
   print(v, end = ' ')
   # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
   for i in graph[v]:
    if not visited[i]:
     queue.append(i)
     visited[i] = True
     
bfs(graph, 1, visited)
```


## Ex

1. 음료수 얼려 먹기

- n * m의 얼음틀이 있을 때, 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주할 때,
 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

- 1 <= N, M <= 1000 
  
  1. DFS
  ```
   n, m = map(int , input().split())
   
   graph = []
   for i in range(n):
    graph.append(list(map(int, input())))
   
   def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
     graph[x][y] = 1      # 해당 노드 방문 처리
     # 상하좌우 위치 재귀적으로 호출
     dfs(x - 1, y)
     dfs(x, y - 1)
     dfs(x + 1, y)
     dfs(x, y + 1)
     return True
    return False
   
   # 모든 노드에 대해 음료수 채우기
   result = 0
   for i in range(n):
    for j in range(m):
     # 현재 위치에서 dfs 수행
     if dfs(i, j) == True: result += 1
     
   print(result)
   
  
   def dfs(x,y)
  ```
  
  2. BFS도 가능

2. 미로 찾기

- n * m의 미로가 있을 때 괴물을 피하면서 탈출을 해야 한다. 현재 위치는 (1, 1)이며 출구는 (n, m)에 존재하며 한 번에 한 칸씩 이동할 수 있다. 괴물을 0 칸에 존재하고 괴물이 없는 부분은 1로 표시되어 있을 때, 탈출하기 위해 움직여야 하는 최소 칸의 개수(시작 칸과 마지막 칸을 모두 포함)를 구하라.

- 4 <= n, m <= 200

  1. BFS를 이용하여 시작 지점부터 가까운 노드 차례대로 그래프의 모든 노드를 탐색하며 모든 노드의 최단 거리 값을 기록하여 해결
  ```
  from collections import deque
  
  n, m = map(int, input().split())
  graph = []
  for i in range(n):
   graph.append(list(map(int, input())))
  
  # 상하좌우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  def bfs(x, y):
   queue = deque()
   queue.append((x, y))
   
   while queue:
    x, y = queue.popleft()
    for i in range(4):
     nx = x + dx[i]
     ny = y + dy[i]
     if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
     if graph[nx][ny] == 0: continue   # 벽
     # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
     if graph[nx][ny] == 1:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx, ny))
   return graph[n - 1][m - 1]
  
  print(bfs(0, 0))
  ``` 



