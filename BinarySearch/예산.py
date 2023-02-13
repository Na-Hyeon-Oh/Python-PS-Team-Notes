# 예산
# https://www.acmicpc.net/problem/2512
'''
국가 예산 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정하려고 한다.
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 있는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
배정된 예산들 중 최댓값인 정수를 출력하라.
* 3 <= N(지방의 수) <= 10,000, 1 <= M(예산) <= 1,000,000,000
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

requests.sort()
upper = 0
left = m // n
right = max(requests)
while left <= right:
  mid = (left + right) // 2
  sum = 0
  for request in requests:
    if request > mid: sum += mid
    else: sum += request
  if sum <= m: 
    upper = mid
    left = mid + 1
  else: right = mid - 1

if max(requests) > upper: print(upper)
else: print(max(requests))
