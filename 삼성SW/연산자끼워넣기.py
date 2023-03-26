# [B_S1] 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
'''
N(2 <= N <= 11)개의 수로 이루어진 수열 A1, A2, .., AN(1 <= Ai <= 100)이 주어지고, N-1개의 연산자 {+, -, *, /}의 개수가 주어진다.
연산의 결과는 앞에서 부터 계산하고, 그ㅡ 결과의 최댓값과 최솟값을 출력하라.
* 시간 제한 2초
* 메모리 제한 512MB
'''

def calculate(n, idx, value,  add, sub, mul, div):
  global maxAns, minAns

  if idx == n - 1: 
    maxAns = max(maxAns, value)
    minAns = min(minAns, value)
    return

  if add > 0: calculate(n, idx + 1, value + a[idx + 1], add - 1, sub, mul, div)
  if sub > 0: calculate(n, idx + 1, value - a[idx + 1], add, sub - 1, mul, div)
  if mul > 0: calculate(n, idx + 1, value * a[idx + 1], add, sub, mul - 1, div)
  if div > 0: calculate(n, idx + 1, value // a[idx + 1] if value >= 0 else (((-1) * (value)) // a[idx + 1]) * (-1), add, sub, mul, div - 1)
  
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxAns = -1000000000
minAns = 1000000000
calculate(n, 0, a[0], add, sub, mul, div)

print(maxAns)
print(minAns)

'''
- 완전탐색(BruteForce)
- 재귀/dfs
'''
