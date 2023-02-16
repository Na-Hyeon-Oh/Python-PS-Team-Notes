# 두 용액
# https://www.acmicpc.net/problem/2470
'''
산성 용액의 특성값은 1~10^9, 알칼리성 용액의 특성값은 -1~-10^9이다.
같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
이 때 특성값이 0에 가까운 용액을 만들려 할 때, 두 용액을 구하시오.
* 2 <= N (전체 용액의 수) <= 100,000
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
liquid = list(map(int, input().split()))

liquid.sort()
min = 1e10
result = []
left = 0
right = len(liquid) - 1
while left < right:
  sum = liquid[left] + liquid[right]
  if abs(min) >= abs(sum) :
    if abs(min) > abs(sum): 
      result.clear()
      min = sum
    result.extend([liquid[left], liquid[right]])
  if sum >= 0: right -= 1
  else: left += 1

print(result[0], result[1])

'''
- 투 포인터
- 용액의 특성값 리스트를 오름차순 정렬한 다음 양끝의 하나씩 0에 가장 가까운 합을 찾아간다.
- 두 용액의 특성값의 합이 양수이면 두번째 용액의 idx를 하나 줄이고(더 작은 특성값), 음수이면 첫번째 용액의 idx를 하나 올린다(더 큰 특성값).
'''
