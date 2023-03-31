# [B_G3] 경사로
# https://www.acmicpc.net/problem/14890
'''
N*N (2 <= N <= 100)의 지도가 있을 때, 각 칸에는 높이가 적혀 있다.
길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같거나, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
경사로의 높이는 1이고, 길이는 L(1 <= L <= N)이고, 경사로는 칸의 높이 차이가 1인 경사로에 바닥이 접한 채로 놓을 수 있다.
지나갈 수 있는 길의 개수를 모두 구하시오.
* 시간 제한 2초
* 메모리 제한 512MB
'''

n, l = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

result = 0
existed = [[0] * n for _ in range(n)]
for i in range(n):
  valid = True
  last = array[i][0]
  for j in range(1, n):
    target = array[i][j]
    if last == target: 
      if j == n - 1: result += 1
    elif abs(last - target) == 1: 
      if target - last > 0:
        for k in range(j - l, j):
          if k >= 0 and array[i][k] == last and existed[i][k] == 0: existed[i][k] = 1
          else:
            valid = False
            break
      else:
        for k in range(j, j + l):
          if k < n and array[i][k] == target and existed[i][k] == 0: existed[i][k] = 1
          else:
            valid = False
            break
      if valid == True and j == n - 1: result += 1
    else: valid = False
    if valid == False: 
      for k in range(n): existed[i][k] = 0
      break
    last = target
for j in range(n):
  valid = True
  last = array[0][j]
  cnt = 1
  for i in range(1, n):
    target = array[i][j]
    if last == target: 
      cnt += 1
      if i == n - 1: result += 1
    elif abs(last - target) == 1: 
      if target - last > 0:
        for k in range(i - l, i):
          if k >= 0 and array[k][j] == last and existed[k][j] != 2: existed[k][j] = 2
          else:
            valid = False
            break
      else:
        for k in range(i, i + l):
          if k < n and array[k][j] == target and existed[k][j] != 2: existed[k][j] = 2
          else:
            valid = False
            break
      if valid == True and i == n - 1: result += 1
    else: valid = False
    if valid == False: 
      for k in range(n): existed[k][j] = 0
      break
    last = target

print(result)



'''
경사로 설치해야 하는 높이 1차이 칸이 있으면 그 때 l만큼 앞 뒤로 검사

- 모듈화 예시 (시간 4ms~8ms 정도 빠름) : https://ryu-e.tistory.com/108
'''
