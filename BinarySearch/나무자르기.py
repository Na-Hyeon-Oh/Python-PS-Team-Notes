# 나무 자르기
# https://www.acmicpc.net/problem/2805
'''
나무가 N개 있을 때, 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
* 1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000
* 제한 시간 1초
'''


# i. PyPy3

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
h = list(map(int, input().split()))

#h.sort()
result = 0
left = 1
right = max(h)
#right = h[-1]
while left <= right:
  mid = (left + right) // 2
  sum = 0
  for tree in h:
    if tree - mid > 0: sum += tree - mid
  if sum >= m:
    result = mid
    left = mid + 1  
  else: 
    right = mid - 1
print(result)


# ii. Python3

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
h = list(map(int, input().split()))

result = 0
left = 1
right = max(h)
while left <= right:
  mid = (left + right) // 2
  if sum(target - mid for target in h if target - mid > 0) >= m:
    result = mid
    left = mid + 1  
  else: 
    right = mid - 1
print(result)


        
'''
- 가능한 M의 범위가 10억으로 매우 크므로 이진 탐색 사용하여야 함
- i.으로는 PyPy3가 아닌 Python3으로는 시간 초과 -> sum함수를 사용하는 것이 더 
'''
