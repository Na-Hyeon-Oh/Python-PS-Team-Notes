# 강의실 배정
# https://www.acmicpc.net/problem/11000
'''
Si~Ti의 N개의 수업이 있을 때, 
최소의 강의실을 사용해 모든 수업을 가능하게 해야 한다.
최소의 강의실 수는?
* 1 <= N <= 200,000
* 시간 제한 1초
'''
import sys
import heapq

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
lectures = []  
for _ in range(n):          # 생성한 lectures 리스트에 heapq의 heappush 메소드를 사용하여 강의 시작/종료 정보 넣기
  heapq.heappush(lectures, list(map(int, input().split())))

classes = []
while lectures:
  lecture = heapq.heappop(lectures)
  if classes:
    if lecture[0] >= classes[0]: heapq.heappop(classes)
  heapq.heappush(classes, lecture[1])

print(len(classes))
  
  
'''
수업 시작과 끝이 최대한 빨라야 한 강의실을 최대로 쓸 수 있으므로 해당 정보에 대해 오름차순 정렬
-> 시간 제한을 맞추기 위해 heapq(priority queue) 사용
생성된 강의실 중 수업이 가장 빨리 끝나는 경우와 비교하면 모든 강의실을 확인할 필요 없음
'''
