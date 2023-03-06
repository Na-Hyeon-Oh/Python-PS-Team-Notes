# [B_S3] 계단 오르기
# https://www.acmicpc.net/problem/2579
'''
계단(<=10,000)을 다음의 규칙으로 오르며 각 계단의 점수를 얻을 때, 얻을 수 있는 총 점수의 최댓값?
1. 계단은 한 번에 한 계단 / 두 계단씩 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. (시작점은 계단에 포함되지 않는다.)
3. 마지막 도착 계단은 반드시 밟아야 한다.
* 시간 제한 1초
* 메모리 제한 128MB
'''

n = int(input())
scores = list(int(input()) for _ in range(n))

if n >= 3:
  dp = [0] * (n + 1)
  dp[1], dp[2], dp[3] = scores[0], scores[0] + scores[1], max(scores[0], scores[1]) + scores[2]
  for i in range(4, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + scores[i - 2]) + scores[i - 1]

  print(dp[n])
elif n == 1: print(scores[0])
elif n == 2: print(max(scores[0] + scores[1], scores[1]))

'''
- 연속으로는 가능하고 세번 연속은 불가능
    - (i번째 계단까지 점수의 최댓값) 
      = (i번째 계단의 점수) + max (i -1 계단과 연속된 경우, 두 번 전의 계단에서 2칸 넘어온 경우)
    - (이전 계단과 연속된 경우의 점수 최댓값) = (i - 1 계단의 점수) + (i - 3 계단까지의 점수 최댓값)
'''
