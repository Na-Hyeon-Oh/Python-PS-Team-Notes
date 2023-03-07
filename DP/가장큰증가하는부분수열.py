# [B_S2] 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055
'''
n개의 정수 (1 <= n <= 1,000, 1 <= Ai <= 1,000)로 이루어진 수열 A이 주어질 때,
몇 개의 수를 선택해서 구할 수 있는 증가하는 부분 수열 중 합의 최댓값?
* 시간 제한 1초
* 메모리 제한 256MB
'''
import sys

def input():
  return sys.stdin.readline()

n = int(input())
a = list(map(int, input().split()))

dp = a.copy()  # dp[i]: i번째 수까지의 증가하는 수열의 최댓값
for i in range(n):
  for j in range(i):
    if a[j] < a[i]:
      dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))

'''
n <= 1,000 => O(N^2)까지 가능
'''
