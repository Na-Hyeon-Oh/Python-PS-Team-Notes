# 공유기 설치
# https://www.acmicpc.net/problem/2110
'''
집 n개가 x1, .., xn의 좌표를 가지고 있다.
각 집에 최대 1개씩 공유기 C개를 설치하려고 할 때, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려 한다.
가장 인접한 두 공유기의 최대 거리는?
* 2 <= N <= 200,000, 2 <= C <= N, 0 <= xi <= 1,000,000,000
* 제한 시간 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()
result = 0
left = 1                  # 최소 거리
right = x[-1] - x[0]      # 최대 거리
while left <= right:
  mid = (left + right) // 2        # 공유기 설치 간
  xi = x[0]               # 앞 집부터 공유기 설치 
  cnt = 1
  for i in range(1, len(x)):
    if x[i] >= xi + mid:
      cnt += 1
      xi = x[i]

  if cnt >= c:            # 더 넓게 설치해야 함
    result = mid
    left = mid + 1        
  else: right = mid - 1   # 더 좁게 설치해야 함

print(result)
  
  


'''
- 구하려고 하는 공유기 사이의 "최소 간격"에 대해 이진 탐색 실시
- xi의 범위 때문에 순차 탐색 시 시간 초과
Ref. https://my-coding-notes.tistory.com/119
'''
