# 파일 합치기 3
# https://www.acmicpc.net/problem/13975
'''
두 파일을 하나의 파일로 합칠 때 필요한 비용은 두 파일 크기의 합이다.
그럴 때 여러 파일을 최종적인 한 개의 파일로 완성할 때 필요한 최소 비용을 구하시오.
* 3 <= K(파일 개수) <= 1,000,000
파일의 크기 <= 10,000
* 시간 제한 2초
'''

import sys
import heapq

def input():
  return sys.stdin.readline().rstrip()

t = int(input())
for i in range(t):
  k = int(input())
  fileSize = list(map(int, input().split()))
  
  result = 0
  heapq.heapify(fileSize)
  while len(fileSize) > 1:
    cost = heapq.heappop(fileSize) + heapq.heappop(fileSize)
    heapq.heappush(fileSize, cost)
    result += cost
  
  print(result)

'''
- list object is not callable error :: 존재하는 method 명과 지정한 변수명이 중복될 경우 발생
- 오름차순 정렬 + pop해야하는 경우 -> 최소힙(heapq) 사용하는 것이 시간초과 안 뜸
; list를 사용하여 매번 pop하고 새로운 리스트로 초기화시키는 것이 시간이 오래 걸림
- heapq.heapify(list) -> list를 heap으로 변환
- 우선순위큐를 사용하여 매번 오름차순 정렬하고 매번 가장 작은 두 수를 더하여 cost로 적립하는 것이 최소 비용
왜냐하면 동일한 파일 사이즈가 중복되어 더해질 수 있는데, 파일 사이즈가 큰 것이 여러 번 더해질 경우 비용이 커질 수 밖에 없음
'''
