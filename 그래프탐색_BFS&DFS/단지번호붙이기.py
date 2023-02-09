# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
'''
정사각형 N * N의 지도가 있을 때, 1은 집이 있는 곳을, 0은 없는 곳을 나타낸다.
한 단지는 상하좌우로 연결되어 있는 경우를 말할 때,
단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하라.
* 5 <= N <= 25
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

def dfs(y, x):
  if x < 0 or x >= n or y < 0 or y >= n: return 0
  if mapInfo[y][x] == "1":
    mapInfo[y][x] = "0"
    cnt = 1
    cnt += dfs(y - 1, x)
    cnt += dfs(y + 1, x)
    cnt += dfs(y, x - 1)
    cnt += dfs(y, x + 1)
    return cnt
  else: return 0
      
n = int(input())
mapInfo = [list(input()) for _ in range(n)]

result = []
for i in range(n):
  for j in range(n):
    cnt = dfs(i, j)
    if(cnt > 0): result.append(cnt)
result.sort()

print(len(result))
for noHome in result: print(noHome)

'''
지도 graph를 탐색하면서 아파트가 존재할 경우 상하좌우를 살피며 몇 개씩 존재하는지 확인하여 dfs()에서 return,
탐색한 위치는 0으로 변환
'''
