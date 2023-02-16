# 입국심사
# https://www.acmicpc.net/problem/3079
'''
M명의 사람이 한 줄로 서서 입국심사를 기다리고 있다.
입국심사대는 총 N개가 있고, k번 심사대에 앉아있는 심사관은 한 명을 심사하는데 Tk의 시간이 든다.
한 입국 심사대에서는 한 번에 한 사람만 심사를 할 수 있을 때, 모든 사람이 심사를 받는데 걸리는 최소 시간을 구하시오.
* 1 <= N <= 100,000, 1 <= M <= 1,000,000,000, 1<= Tk <= 10^9
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

result = 1
left = 1
right = max(t) * m
while left <= right:
  mid = (left + right) // 2
  target = 0
  for tk in t:
    target += mid // tk
  if target >= m:
    result = mid
    right = mid - 1
  else:
    left = mid + 1

print(result)

'''
- 시간의 최솟값을 1, 최댓값을 가장 큰 tk에 m을 곱한 값으로 두고 해당 시간의 최솟값을 최적화하는 문
'''
