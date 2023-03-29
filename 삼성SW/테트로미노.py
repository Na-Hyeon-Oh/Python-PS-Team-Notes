# [B_G4] 테트로미노
# https://www.acmicpc.net/problem/14500
'''
N*M (4 <= N, M <= 500) 종이 위에 테트로미노 하나를 놓을 때, 각 칸의 정수(<= 1,000)의 합이 최대가 되도록 하는 프로그램
* 시간 제한 2초
* 메모리 제한 512MB
'''

def getT(n, m):
  global maxSum

  # type 1-1 (1, 4)
  for i in range(n):
    for j in range(m - 3):
      t = arr[i][j]
      for k in range(1, 4): t += arr[i][j + k]
      maxSum = max(maxSum, t)
  # type 1-2 (4, 1)
  for j in range(m):
    for i in range(n - 3):
      t = arr[i][j]
      for k in range(1, 4): t += arr[i + k][j]
      maxSum = max(maxSum, t)

  # type 2 (2, 2)
  for i in range(n - 1):
    for j in range(m - 1):
      t = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
      maxSum = max(maxSum, t)

  # type 3-1 (3, 2) ㄱ/ㄴ
  for i in range(n - 2):
    for j in range(m - 1):
      t1 = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
      t2 = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i + 2][j]
      t3 = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1]
      t4 = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i][j]
      maxSum = max(maxSum, t1, t2, t3, t4)
  # type 3-2 (2, 3)
  for j in range(m - 2):
    for i in range(n - 1):
      t1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]
      t2 = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i][j + 2]
      t3 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]
      t4 = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i][j]
      maxSum = max(maxSum, t1, t2, t3, t4)

  # type 4-1 (3, 2) s
  for i in range(1, n - 1):
    for j in range(m - 1):
      t = arr[i][j] + arr[i][j + 1]
      t1 = t + arr[i - 1][j] + arr[i + 1][j + 1]
      t2 = t + arr[i - 1][j + 1] + arr[i + 1][j]
      maxSum = max(maxSum, t1, t2)
  # type 4-2 (2, 3)
  for j in range(1, m - 1):
    for i in range(n - 1):
      t = arr[i][j] + arr[i + 1][j]
      t1 = t + arr[i][j - 1] + arr[i + 1][j + 1]
      t2 = t + arr[i + 1][j - 1] + arr[i][j + 1]
      maxSum = max(maxSum, t1, t2)

  # type 5-1 (3, 2) ㅏ
  for i in range(n - 2):
    for j in range(m - 1):
      t1 = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j + 1]
      t2 = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i + 1][j]
      maxSum = max(maxSum, t1, t2)
  # type 5-2 (2, 3) ㅗ
  for j in range(m - 2):
    for i in range(n - 1):
      t1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
      t2 = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i][j + 1]
      maxSum = max(maxSum, t1, t2)

# 동, 남
dx = [0, 1]
dy = [1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
getT(n, m)

print(maxSum)

'''
그래프탐색을 활용하려 하였으나 type 5와 같은 케이스를 처리하지 못해, 각 테트로미노 모양에 대해 가질 수 있는 합을 모두 구현해주었다.
'''
