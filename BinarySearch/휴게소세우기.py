# 휴게소 세우기
# https://www.acmicpc.net/problem/1477
'''
현재 고속도로에 휴게소를 N개 가지고 있을 때, 휴게소의 위치는 고속도로의 시작으로부터 얼만큼 떨어져 있는지로 주어진다. 
휴게소 M개를 더 세우려고 할 때, 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려 한다.
단, 이미 휴게소가 있는 곳에 다시 휴게소를 세울 수 없고, 고속도로의 끝에도 세울 수 없다.
휴게소가 없는 구간의 최댓값의 최솟값은 ?
* 0 <= N <= 50, 1 <= M <= 100, 100 <= L <= 1,000, 1 <= 휴게소의 위치 <= L - 1
* 제한 시간 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m, l = map(int, input().split())
loc = [0] + list(map(int, input().split())) + [l]        # 출발지점, 도착 지점 포함

loc.sort()
result = 0
left = 1
right = l - 1
while left <= right:
  mid = (left + right) // 2
  cnt = 0
  for i in range(1, len(loc)):
    if loc[i] - loc[i-1] > mid:                # 휴게소 간 거리 중 mid보다 큰 거리에 대해서
      cnt += (loc[i] - loc[i-1] - 1) // mid    # 휴게소 설치 가능한 영역 나누기(몇 개의 휴게소를 설치할 수 있는가)

  if cnt > m:                          # mid는 더 길어야 할 때
    left = mid + 1
  else:                                # mid는 더 짧아야 할 때 -> 이 때까지의 최솟값 저장
    result = mid
    right = mid - 1

print(result)


'''
구하려고 하는 것은 휴게소가 없는 구간 거리의 최댓값 -> 이에 대한 이진 탐색
최악의 경우 L * L ~= 1e6만큼의 연산 필요
* ~한 최댓값의 최솟값 -> mid가 짧아져야 할 때 result 저장
* ~한 최솟값의 최댓값 -> mid가 길어져야 할 때 result 저장
'''
