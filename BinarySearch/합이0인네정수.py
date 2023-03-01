# [B_G2] 합이 0인 네 정수
# https://www.acmicpc.net/problem/7453
'''
크기가 같은 정수로 이루어진 배열 A, B, C, D가 있을 때
A[a] + B[b] + C[c] + D[d] = 0인 쌍의 개수를 구하라
* 1 <= N(배열의 크기) <= 4000, 배열 원소 <= 2^28
* 제한 시간 12초
'''

# i.

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
  ai, bi, ci, di = map(int, input().split())
  a.append(ai)
  b.append(bi)
  c.append(ci)
  d.append(di)

abCase = dict()
for i in range(n):
  for j in range(n):
    abCase.update({a[i] + b[j]: 1 if abCase.get(a[i] + b[j]) is None else abCase.get(a[i] + b[j]) + 1})
result = 0
for i in range(n):
  for j in range(n):
    sum = -(c[i] + d[j])
    if sum in abCase.keys():
      result += abCase[sum]

print(result)


# ii.

import sys

def input():
  return sys.stdin.readline().rstrip()


n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
  ai, bi, ci, di = map(int, input().split())
  a.append(ai)
  b.append(bi)
  c.append(ci)
  d.append(di)

abCase = []
cdCase = []
for i in range(n):
  for j in range(n):
    abCase.append(a[i] + b[j])
    cdCase.append(c[i] + d[j])
abCase.sort()
cdCase.sort()
result = 0
i, j = 0, n**2 - 1  # 투포인터
while i < n**2 and j >= 0:
  sum = abCase[i] + cdCase[j]
  if sum == 0:
    x, y = i + 1, j - 1
    # 연속된 수의 case 처리
    while x < n**2 and abCase[i] == abCase[x]:
      x += 1
    while y >= 0 and cdCase[j] == cdCase[y]:
      y -= 1
    result += (x - i) * (j - y)
    i, j = x, y
  elif sum > 0:
    j -= 1
  else:
    i += 1

print(result)


'''
PyPy3
i - 1.
- A, B 배열로 만들 수 있는 합, C, D 배열로 만들 수 있는 합 -> dict에 hash값으로 저장 (2 * O(n^2 * 1))
    * dictionary update : (dict).update({(key): (value)})
- 각 dictionary에 해당하는 경우를 구하면 서로 대응되는 값이 있는지 각각 탐색 -> hash -> O(n^2 * 1)
=> 시간 초과 (O(3 * n^2))
i - 2.
A, B 배열로 만들 수 있는 dict만 만들고, C, D 배열로 만들 수 있는 경우는 abCase의 key값을 이용하여 바로 확인 -> (2 * O(N^2 * 1))

ii. 투포인터 이용
- A, B 배열로 만들 수 있는 합, C, D 배열로 만들수 있는 합을 list에 각각 저장 -> O(n^2 + 2)
- 정렬 -> 2 * O(n log n)
- abCase는 처음부터(음수쪽부터), cdCase는 마지막부터(양수쪽부터) 각각의 합이 0인 케이스의 개수 합하기 -> O(n)
'''
