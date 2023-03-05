# [B_S3] 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
'''
정수 n ( < 11) 이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램
* 시간 제한 1초
* 메모리 제한 512MB
'''

t = int(input())
for _ in range(t):
  n = int(input())

  dp = [0] * n                      # dp[i] = i를 1, 2, 3으로 만드는 경우의 수
  if n >= 3:
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, n):
      dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n - 1])
  elif n == 2: print(2)
  elif n == 1: print(1)
