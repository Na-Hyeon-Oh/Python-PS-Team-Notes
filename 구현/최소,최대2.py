# 최소, 최대 2
# https://www.acmicpc.net/problem/20053
'''
N개의 정수가 주어질 때, 최솟값과 최댓값 구하는 프로그램 작성하기
* 1 <= N <= 1,000,000, 1 <= T <= 10
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline()

t = int(input())
for _ in range(t):
  n = int(input())
  nums = list(map(int, input().split()))
  print(f'{min(nums)} {max(nums)}')

'''

'''
