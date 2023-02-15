# 랜선 자르기
# https://www.acmicpc.net/problem/1654
'''
랜선이 K개 있을 때, N개(혹은 이상)의 같은 정수 길이의 랜선으로 만든다고 할 때, 최대 랜선의 길이를 구하는 프로그램
* K <= N, 1 <= K <= 10,000, 1 <= N <= 1,000,000, 랜선의 길이 <= 2^31 - 1
* 제한 시간 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

k, n = map(int, input().split())
h = [int(input()) for _ in range(k)]

h.sort()
result = 0
left = 1
right = h[-1]
while left <= right:
  mid = (left + right) // 2
  count = 0
  for lan in h:
    count += lan // mid
  if count < n:
    right = mid - 1
  else:
    result = mid
    left = mid + 1
    
print(result)

'''
- 랜선의 길이는 자연수이므로 따라 답이 0이 될 수 없으므로 left는 1부터
'''
