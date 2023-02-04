# 상어 초등학교
# https://www.acmicpc.net/problem/21608
'''
교실은 N * N 크기이고, 학생 수는 N^2이다.
각 학생은 4명의 좋아하는 학생이 있다.
(r, c)는 r행 c열을 의미할 때, 가장 좌측상단의 자리는 (1,1)이고 우측하단의 자리는 (N, N)이다.
다음의 조건을 이용하여 자리를 정한다고 했을 때, 학생의 최대 만족도를 구하시오.
1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸이 여러 개이면, 행의 번호가 가장 작은 칸으로 자리를 정한다.
4. 3을 만족하는 칸이 여러 개이면, 열의 번호가 가장 작은 칸으로 자리를 정한다.
* 학생의 만족도 : 학생과 인접한 칸에 앉은 좋아하는 학생의 수
* 3 <= N <= 20
* 제한 시간 1초
'''


import sys

def input():
  return sys.stdin.readline()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
students = [list(map(int, input().split())) for _ in range(n*n)]

seats = [[0 for _ in range(n)] for _ in range(n)]
for student in students:
  id = student[0]
  adjacency = []             # (좋아하는 학생 수, 비어있는 칸 수, -r, -c)
  for r in range(n):
    for c in range(n):
      likes = 0
      empties = 0
      for i in range(4):     # 인접한 칸 탐색
        nx = c + dx[i]
        ny = r + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
          if seats[ny][nx] == 0: empties += 1
          else:
            for s in range(1, 5):
              if seats[ny][nx] == student[s]: 
                likes += 1
                break
      adjacency.append([likes, empties, -r, -c])
  adjacency.sort(reverse=True)
  for element in adjacency:
    if seats[-element[2]][-element[3]] == 0: 
      seats[-element[2]][-element[3]] = id
      break

result = 0
for r in range(n):
  for c in range(n):
    for student in students:
      if student[0] == seats[r][c]:
        likes = 0
        for i in range(4):
          nx = c + dx[i]
          ny = r + dy[i]
          if 0 <= nx < n and 0 <= ny < n:
            for s in range(1, 5):
              if seats[ny][nx] == student[s]: 
                likes += 1
                break
        if likes == 1: result += 1
        elif likes == 2: result += 10
        elif likes == 3: result += 100
        elif likes == 4: result += 1000

print(result)

'''

'''
