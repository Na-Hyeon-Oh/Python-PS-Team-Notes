# 배열 돌리기 1
# https://www.acmicpc.net/problem/16926
'''
n*m 크기의 배열이 있을 때, 각 원소를 r번 반시계 방향으로 한 칸씩 회전시켰을 때의 결과
* 2 <= n, m <= 300, 1 <= r <= 1,000
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
a = [list(input().split()) for _ in range(n)]

i = 0
while i < min(n, m) // 2:
  tmp = []
  for x in range(m - 2 * i): tmp.append(a[i][x + i])
  for y in range(1, n - 2 * i): tmp.append(a[y + i][m - 1 - i])
  for x in range(1, m - 2 * i): tmp.append(a[n - 1 - i][m - 1 - x - i])
  for y in range(1, n - 2 * i - 1): tmp.append(a[n - 1 - y - i][i])

  # move
  for _ in range(r):
    element = tmp.pop(0)
    tmp.append(element)

  # save
  dir = 0
  cnt = 0
  for element in tmp:
    if dir == 0:
      a[i][cnt + i] = element
      if cnt == m - 2 * i - 1: 
        dir += 1
        cnt = 0
    elif dir == 1:
      a[cnt + i][m - 1 - i] = element
      if cnt == n - 2 * i - 1:
        dir += 1
        cnt = 0
    elif dir == 2:
      a[n - 1 - i][m - 1 - cnt - i] = element
      if cnt == m - 2 * i - 1: 
        dir += 1
        cnt = 0
    elif dir == 3: a[n - 1 - cnt - i][i] = element  
    cnt += 1
    
  i += 1

for row in a:
  print(' '.join(row))


'''
- 반시계방향으로 돌리는 경우를 각 리스트로 저장하여 모두 돌린 후, 다시 Aij에 저장
'''
