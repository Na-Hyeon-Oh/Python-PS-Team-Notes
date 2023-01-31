# 윤년
# https://www.acmicpc.net/problem/2753
'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램
- 윤년 : 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline()

year = int(input())
isLeapYear = 0
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): isLeapYear = 1

print(isLeapYear)

'''

'''
