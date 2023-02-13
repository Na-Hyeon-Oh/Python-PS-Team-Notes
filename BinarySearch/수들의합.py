# 수들의 합
# https://www.acmicpc.net/problem/1789
'''
서로 다른 N개의 자연수의 합이 S라고 할 때, 자연수 N의 최댓값?
* 1 <= S <= 4,294,967,295
* 제한 시간 2초
'''

#i.
import sys

def input():
  return sys.stdin.readline().rstrip()

s = int(input())

n = 1
left = 1      # 최솟값
right = s     # 최댓값
while left <= right:
  mid = (left + right) // 2
  if mid * (mid + 1) // 2 <= s:
    n = mid
    left = mid + 1
  else:
    right = mid - 1
    
print(n)


#ii.
import sys

def input():
  return sys.stdin.readline().rstrip()

s = int(input())

n = 1
while n * (n + 1) / 2 <= s:
  n += 1
n = n - 1
print(n)
