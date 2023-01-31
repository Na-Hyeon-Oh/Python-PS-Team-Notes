# 8진수 2진수
# https://www.acmicpc.net/problem/1212
'''
8진수가 주어졌을 때, 2진수로 변환하는 프로그램 작성하기
* 8진수로 주어지는 수의 길이 <= 333,334
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline()

print(bin(int(input(), 8))[2:])


'''
8진수 -> 10진수 -> 2진수
- string을 저장하면 \n도 함께 저장되어 실제 길이 + 1의 길이가 len(str)로 반환됨
- int(input(), n) -> n진법으로 받음
- bin(int) -> 2진수로 변환
'''
