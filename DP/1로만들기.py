# [B_S3] 1로 만들기
# https://www.acmicpc.net/problem/1463
# README.md 참고

x = int(input())
bigNum = 1e8

dp = [0] * x
for i in range(1, x):
  target = i + 1
  dp[i] = min((dp[target // 3 - 1] + 1 if target % 3 == 0 else bigNum), (dp[target // 2 - 1] + 1 if target % 2 == 0 else bigNum), dp[i - 1] + 1)

print(dp[x - 1])
