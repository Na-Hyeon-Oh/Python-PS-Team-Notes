# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
'''
두 파일을 하나의 파일로 합칠 때 필요한 비용은 두 파일 크기의 합이다.
그럴 때 여러 파일을 최종적인 한 개의 파일로 완성할 때 필요한 최소 비용을 구하시오.
* 1 <= N <= 100,000
파일의 크기 <= 1,000
* 시간 제한 2초
'''

import sys
import heapq

def input():
  return sys.stdin.readline()

n = int(input())
heap = []
for _ in range(n): heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    compare = heapq.heappop(heap) + heapq.heappop(heap)
    result += compare
    heapq.heappush(heap, compare)

print(result)

'''
# 파일 합치기 3과 사실상 같은 문제
'''
