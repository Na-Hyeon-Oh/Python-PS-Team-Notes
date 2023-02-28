# K번째 수
# https://www.acmicpc.net/problem/1300
'''
N * N 크기의 배열 A가 있고 A[i][j] = i * j이다.
이를 일차원 배열 B에 넣고 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.
* N <= 10^5, k <= min(10^9, N^2)
* 제한 시간 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())

result = 1
start = 1
end = n * n
while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for i in range(1, n + 1):
    cnt += min(mid // i, n)

  if cnt >= k:
    result = mid
    end = mid - 1
  else:
    start = mid + 1

print(result)

'''
어떤 수를 기준으로 해당 수보다 작은 수 개수 구하기
- 아래의 코드는 최악의 경우 O(n * n) -> 시간 초과
 ```
 for i in range(1, min(n + 1, mid + 1)):
    for j in range(1, min(n + 1, mid + 1)):
      if i * j < mid: cnt += 1
      else: break
 ```
- 예를 들어 10*10 행렬에서 20보다 작은 수는
  { 1 * 1 ~ 1 * 10, 2 * 1 ~ 2 * 10, 3 * 1, 3 * 6, .. 10 * 1 ~ 10 * 2 }
  -> { 10, 10, 6, .. 2}
  -> { min(20 // 1, 10), min(20 // 2, 10), min(20 // 3, 10), ... min(20 // 10, 10) }
'''
