# [B_G1] 구슬 탈출 2
# https://www.acmicpc.net/problem/2294
'''
N * M (3 <= N, M <= 10) 크기의 보드(.: 빈칸, #: 장애물/벽)에 구멍(O)이 하나 있고 빨간 구슬(R)과 파란 구슬(B)이 하나씩 들어 있다고 할 때, 빨간 구슬을 구멍을 통해 빼내야 한다.
왼쪽이나 오른쪽, 위쪽, 아래쪽으로 기울이기를 통해 구슬을 중력을 이용해 굴린다고 할 때,
최소 몇번만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지?
단, 파란 구슬이 구멍에 빠지면 안되고, 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
* 시간 제한 2초
* 메모리 제한 512MB
'''

from collections import deque

LIMIT = 10
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(rx, ry, bx, by):
  q = deque()
  q.append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  cnt = 0
  while q:
    for _ in range(len(q)):
      rx, ry, bx, by = q.popleft()
      if cnt > LIMIT:                               # 10번 넘게 방향을 조정해야 하는 경우
        print(-1)
        return
      if graph[rx][ry] == 'O':                      # Red가 가장 먼저 도착하는 경우
        print(cnt)
        return

      for i in range(4):                            # Red, Blue의 도착지점 구하기 
        rnx, rny = rx, ry
        while True:
          rnx += dx[i]
          rny += dy[i]
          if graph[rnx][rny] == '#':
            rnx -= dx[i]
            rny -= dy[i]
            break
          elif graph[rnx][rny] == 'O': break
        bnx, bny = bx, by
        while True:
          bnx += dx[i]
          bny += dy[i]
          if graph[bnx][bny] == '#':
            bnx -= dx[i]
            bny -= dy[i]
            break
          elif graph[bnx][bny] == 'O': break
        if graph[bnx][bny] == 'O': continue              # Blue가 먼저 구멍에 들어가거나 동시에 들어가는 경우 방지
        if rnx == bnx and rny == bny:                   # 두 구슬 위치 같을 경우, 더 많이 이동한 구슬이 더 늦게 도착 -> 위치 보정
          if abs(rnx - rx) + abs(rny - ry) > abs(bnx - bx) + abs(bny - by):
            rnx -= dx[i]
            rny -= dy[i]
          else:
            bnx -= dx[i]
            bny -= dy[i]        
        if (rnx, rny, bnx, bny) not in visited:         # queue에 추가
          q.append((rnx, rny, bnx, bny))
          visited.append((rnx, rny, bnx, bny))
    cnt += 1
  print(-1)
      
# Red, Blue 위치 찾기
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
  for j in range(m):
    match graph[i][j]:
      case 'R': rx, ry = i, j
      case 'B': bx, by = i, j
      case _: pass

bfs(rx, ry, bx, by)


'''
*** 다시 풀어보기
- #이나 O가 나오는 곳까지 이동 후 같은 row/column에서 이동 시, 더 멀리서 온 구슬 좌표 보정
- 각 방향으로의 Red, Blue의 이동을 매번 cnt 해주면 안되고 한 level당 1씩 cnt 
'''
