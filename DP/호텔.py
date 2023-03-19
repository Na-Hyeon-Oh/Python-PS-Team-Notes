# [B_G5] 호텔
# https://www.acmicpc.net/problem/1106
'''
홍보를 할 수 있는 도시 N개 (<= 20)가 주어지고, 각 도시별로 홍보하는데 드는 비용 (<= 100)과 그 때 몇 명의 호텔 고객 (<= 100)이 늘어나는지에 대한 정보가 있다.
고객을 적어도 C명(<= 1,000) 늘리기 위해 투자해야 하는 비용의 최솟값?
* 시간 제한 2초
* 메모리 제한 128MB
'''

import sys

def input():
  return sys.stdin.readline()

c, n = map(int, input().split())
array = [list(map(int,input().split())) for _ in range(n)]

dp = [1e7] * (c + 100)             # c명을 만들기 위해 필요한 최소 cost
dp[0] = 0

for cost, client in array:
  for i in range(client, c + 100):
    dp[i] = min(dp[i - client] + cost, dp[i])

print(min(dp[c:]))

  
'''
https://bio-info.tistory.com/218#2._%ED%95%B5%EC%8B%AC_%EB%85%BC%EB%A6%AC%E2%98%A2%EF%B8%8F
'''
