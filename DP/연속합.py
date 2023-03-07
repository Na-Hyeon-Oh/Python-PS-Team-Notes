# [B_S2] 연속합
# https://www.acmicpc.net/problem/1912
'''
n개의 정수 (1 <= n <= 100,000, -1,000 <= 수 <= 1,000)로 이루어진 임의의 수열이 주어질 때,
연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합?
* 시간 제한 1초
* 메모리 제한 128MB
'''
import sys

def input():
  return sys.stdin.readline()

n = int(input())
nums = list(map(int, input().split()))

dp = nums.copy()                        # dp[i]: i번째 수까지의 최댓값
for i in range(1, n):
  dp[i] = max(dp[i], dp[i-1] + dp[i])

print(max(dp))

'''
n <= 1,000 -> O(N^2)은 시간 초과
    CF. dp = nums.copy()  # dp[i] : i번째 수에서 시작하는 연속된 수의 합 중 최댓값
        for i in range(n):
          maxSum = nums[i]
          sum = nums[i]
          for j in range(i + 1, n):
            sum += nums[j]
            maxSum = max(maxSum, sum)
          dp[i] = maxSum
'''
