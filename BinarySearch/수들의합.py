# 1

import sys

def input():
  return sys.stdin.readline().rstrip()

s = int(input())

n = 1
while n * (n + 1) / 2 <= s:
  n += 1
n = n - 1
print(n)
