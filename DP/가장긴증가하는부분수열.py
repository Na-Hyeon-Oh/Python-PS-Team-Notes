# [B_S2] 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
'''
수열 A (1 <= N(수열 크기) <= 1,000, 1 <= Ai <= 1,000) 가 주어졌을 때,
가장 긴 증가하는 부분 수열을 구하는 프로그램
* 시간 제한 1초
* 메모리 제한 256MB
'''

n = int(input())
a = list(map(int, input().split()))

dp = [1] * (n)                    # dp[i]: i번째 ai로 끝나는 수열 중에 가장 긴 수열의 크기
for i in range(1, n):
  for j in range(0, i):
    if a[j] < a[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

'''
- LIS 문제
- 최악의 경우 O(N^2)
'''
