# 세 용액
# https://www.acmicpc.net/problem/2473
'''
산성 용액의 특성값은 1 ~ 1,000,000,000까지의 양의 정수, 알칼리성 용액의 특성값은 -1 ~ -1,000,000,000까지의 음의 정수로 나타낼 때,
같은 양의 세 가지 용액을 혼합한 용액의 특성값은 각 용액의 합으로 정의한다.
같은 양의 세 가지 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어라.
* 3 <= N(전체 용액의 수) <= 5,000 
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

def binarySearch(start, end):
  min = 1e10
  while end - start > 1:
    sum = liquids[start] + liquids[end]
    minSum = 1e10
    minMid = start + 1
    for mid in range(start + 1, end):
      if abs(sum + liquids[mid]) < abs(minSum): 
        minMid = mid
        minSum = sum + liquids[mid]
    sum += liquids[minMid]
    if abs(sum) < abs(min):
      result.clear()
      result.extend([liquids[start], liquids[minMid], liquids[end]])
      min = sum
    
    if sum == 0: break
    elif sum > 0: end -= 1
    else: start += 1
  return result

n = int(input())
liquids = list(map(int, input().split()))

liquids.sort()
result = []
left = 0
right = n - 1
binarySearch(left, right)

print(*result)

'''
- 두 용액을 먼저 선택한 뒤 그 사이의 용액 중 전체 용액의 특성값이 최소가 되는 하나의 용액 설정
'''
