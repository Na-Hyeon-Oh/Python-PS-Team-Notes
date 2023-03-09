# [B_S2] 가장 긴 짝수 연속한 부분 수열 (small)
# https://www.acmicpc.net/problem/22859
'''
n개의 정수 (1 <= n <= 50,000, 1 <= Si <= 10^6)로 이루어진 수열 S가 주어질 때,
최대 K번 (1 <= K <= 100)번 원소를 삭제한 수열에서
짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이?
* 시간 제한 1초
* 메모리 제한 1024MB
'''

import sys

def input():
  return sys.stdin.readline()

n, k = map(int, input().split())
s = list(map(int, input().split()))

# i. 

dp = [0] * n                  # dp[i]: i번째 수로 시작하는 수열의 최대 짝수 개수
for i in range(n):
  cnt = 0
  for j in range(i, n):
    if s[j] % 2 == 0: dp[i] += 1
    else: cnt += 1
    if cnt > k: break;

print(max(dp))


# ii. 

dp = [0]                  # dp[i]: i번째 수로 시작하는 수열의 최대 짝수 개수
for i in range(n):
  if s[i] % 2 == 0: dp[-1] += 1          # 짝수 : 마지막에 1 더하기
  else: dp.append(dp[-1])                # 홀수 : 마지막 원소 추가하기
result = dp[:k+1][-1]                     # 최대 k개를 뺐을 때 짝수 수열 
for i in range(k + 1, len(dp)):
  if dp[i] - dp[i - (k + 1)] > result:        # dp[i] - dp[i - (k + 1)] : 짝수 개수
    result = dp[i] - dp[i - (k + 1)]

print(result)


'''
i. PyPy3
- O(N^2)

ii. Python
- O(N)
'''
