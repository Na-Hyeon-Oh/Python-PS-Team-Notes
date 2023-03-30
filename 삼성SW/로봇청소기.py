# [B_G5] 로봇 청소기
# https://www.acmicpc.net/problem/14503
'''
N*M (3 <= N, M <= 50) 크기의 방에서 로봇 청소기는 바라보는 방향이 있고 0, 1은 각각 청소되지 않은 상태, 벽을 나타낼 때 다음과 같이 작동한다.
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
  1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
  2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
  1. 반시계 방향으로 90도 회전한다.
  2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
  3. 1번으로 돌아간다.
청소하는 칸의 개수는 ?
* 시간 제한 2초
* 메모리 제한 512MB
'''

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

result = 0
while True:
  if room[r][c] == 0: 
    result += 1
    room[r][c] = 2
  if room[r - 1][c] != 0 and room[r][c + 1] != 0 and room[r + 1][c] != 0 and room[r][c - 1] != 0: 
    if room[r - dr[d]][c - dc[d]] != 1:
      r = r - dr[d]
      c = c - dc[d]
    else: break          # 종료 조건 
  else:
    d = (d + 3) % 4        # 반시계 방향으로 90도 회전했을 때 다음 방향
    if room[r + dr[d]][c + dc[d]] == 0:
      r = r + dr[d]
      c = c + dc[d]

print(result)
