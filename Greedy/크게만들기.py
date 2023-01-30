# 크게 만들기
# https://www.acmicpc.net/problem/2812
'''
N자리 숫자가 주어졌을 때, 숫자 K개를 지워 얻을 수 있는 가장 큰 수
* 1 <= K < N <= 500,000
* 시간 제한 1초
'''

import sys

def input():
  return sys.stdin.readline()

n, k = map(int, input().split())
num = list(input())                    # empty separator('') 기준 list 만들기

idx = 0
buf = []          # 자동 오름차순 stack
for idx in range(n):
  while len(buf) > 0 and len(buf) + n - idx > n - k and buf[-1] < num[idx]:       # pop 조건 및 pop 종료 조건
    buf.pop()
  buf.append(num[idx])
  idx += 1
  
result = ''.join(buf[:n-k])                  # list -> string     # n-k까지만 (ex) n = 2, k = 1, num = 10
print(result)

'''
- 큰 수를 결정하는 것은 앞 자리 수 -> 앞부터 하나씩 차례대로 검사하며 다음 숫자와 비교했을 때 더 큰 수이면 stack에 남기고, 더 작은 수이면 지운다.
stack은 자동 내림차순으로 정렬된다.
    - list.pop()은 자동으로 stack처럼 LIFO 역할
- ord() 함수 없어도 string 끼리 대소비교 가능
- list를 stack 대신 사용하게 되면 시간 초과가 난다.
'''
