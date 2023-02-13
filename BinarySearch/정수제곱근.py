# 정수 제곱근
# https://www.acmicpc.net/problem/2417
'''
정수(n)가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램
* 0 <= n <= 2^63
* 제한 시간 0.4초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

result = 0
left = 1
right = n
while left <= right:
  mid = (left + right) // 2
  if mid * mid < n: left = mid + 1
  else: 
    result = mid
    right = mid - 1

print(result)


'''
.sqrt()를 이용하는 것보다 빠름
'''
