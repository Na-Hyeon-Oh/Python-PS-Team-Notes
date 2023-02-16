# 색종이와 가위
# https://www.acmicpc.net/problem/20444
'''
색종이를 자를 때 다음의 규칙을 따를 때, n번의 가위질로 k개의 색종이 조각을 만들 수 있는가?
1. 색종이는 직사각형이며, 색종이를 자를 때는 한 변에 평행하게 자른다.
2. 자르기 시작했으면, 경로 상의 모든 색종이를 자를 때까지 멈추지 않는다.
3. 이미 자른 곳을 또 자를 수 없다.
* 1 <= n <= 2^31 - 1, 1 <= k <= 2^63 - 1
* 제한 시간 0.1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

result = False
left = 0
right = n // 2
while left <= right:
  row = (left + right) // 2
  col = n - row
  pieces = (row + 1) * (col + 1)
  if pieces == k: 
    result = True
    break
  elif pieces < k: left = row + 1
  else: right = row - 1
  
if result: print("YES")
else: print("NO")

'''
- 시간 제한이 0.1초이므로 log n의 시간복잡도를 가지는 알고리즘 사용해야 - 이진탐색
- 0 <= row <= n // 2의 범위만 정해지만 col은 자동으로 n - row로 정해짐
'''
