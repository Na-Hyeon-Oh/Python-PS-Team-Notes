# 우체국
# https://www.acmicpc.net/problem/2141
'''
N개의 마을 이 있을 때, 각 마을의 위치와 인구는 X[i], A[i]이다.
하나의 우체국을 세우려고 할 때, 각 마을의 사람까지의 합이 최소가 되는 위치에 우체국을 세우려고 한다.
이 때, 우체국을 세울 위치를 구하는 프로그램을 작성하시오
* 3 <= N <= 100,000
0 <= (X, A) <= 1,000,000,000
* 시간 제한 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
xa = [list(map(int, input().split())) for _ in range(n)]
xa.sort()          # sortedXA = sorted(xa, key=lambda xa:xa[0])    # 첫번째 원소가 중복되지 않으므로 key를 xa[0]으로 둔 것과 같은 효과

population = 0
for i in range(n): population += xa[i][1]

sum = 0
for i in range(n):
  sum += xa[i][1]
  if sum >= int((population + 1) / 2):        # 인원 수가 많은 쪽에 우체국 
    print(xa[i][0])
    break


'''
- xi 기준 오름차순 정렬
- 좌우의 인구를 하나씩 비교하면서 인구 수 비슷하게 유지 -> 전체의 인구 절반이 좌측 마을에 위치
'''
