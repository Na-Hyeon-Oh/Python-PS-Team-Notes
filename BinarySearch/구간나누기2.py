# 구간 나누기 2
# https://www.acmicpc.net/problem/1477
'''
N개의 수로 이루어진 1차원 배열이 있을 때, M개의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 하려 한다.
구간은 다음의 조건을 만족한다.
1. 하나의 구간은 하나 이상의 연속된 수(배열 상)로 이루어져 있다.
2. 배열의 각 수는 모두 하나의 구간에 포함되어 있어야 한다.
* 구간의 점수 = 각 구간에 속한 수의 최댓값 - 최솟값
* 1 <= N <= 5,000, 1 <= M <= N, 1 <= 배열의 element <= 10,000
* 제한 시간 2초
'''

# i. 
import sys

def input():
  return sys.stdin.readline().rstrip()

def binarySearch(start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    groupNo = 1
    currentGroup = []
    for element in array:              # array의 값 하나씩 검사
      if len(currentGroup) == 0 or max(max(currentGroup), element) - min(min(currentGroup), element) <= mid:            # 현재 확인 중인 group에 포함될 수 있는지 (mid의 구간 점수를 유지할 수 있는지)
        currentGroup.append(element)
      else:
        currentGroup = [element]
        groupNo += 1
        
    if groupNo > m:            # group 개수가 많으면 줄일 수 있도록 mid를 키우기
      start = mid + 1
    else:                      # group 개수가 m 이하이면 그 최솟값까지 계속 mid를 줄이기
      result = mid
      end = mid - 1
  return result

n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = max(array) - min(array)
print(binarySearch(left, right))


# ii. (i. 정리된 버전)

import sys

def input():
  return sys.stdin.readline().rstrip()

def binarySearch(start, end, n):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    groupNo = 1
    minNum = maxNum = array[0]
    for i in range(1, n):              # array의 값 하나씩 검사
      minNum = min(minNum, array[i])
      maxNum = max(maxNum, array[i])
      if maxNum - minNum > mid: 
        groupNo += 1  
        minNum = maxNum = array[i]
    if groupNo > m:            # group 개수가 많으면 줄일 수 있도록 mid를 키우기
      start = mid + 1
    else:                      # group 개수가 m 이하이면 그 최솟값까지 계속 mid를 줄이기
      result = mid
      end = mid - 1
  return result

n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = max(array) - min(array)
print(binarySearch(left, right, n))

'''
구하려고 하는 것은 구간 점수의 최댓값의 최솟값 -> 최악의 경우 N * 10000 ~= 1e7만큼의 연산 필요 -> 이진 탐색
- 구간을 주어진 배열의 연속된 수로 나누는 것이므로 임시 이진 탐색 값인 mid를 정답으로 간주하고 array를 모두 검사하였을 때, mid가 적절한지 확인해주는 방식
'''
