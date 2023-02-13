# 숫자 카드
# https://www.acmicpc.net/problem/10815
'''
N개의 숫자 카드를 가지고 있고, 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 가지고 있는지 구하는 프로그램
* 1 <= N, M <= 500,000, -10,000,000 <= 숫자카드의 수 <= 10,000,000
* 제한 시간 2초
'''

#i.
import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()
for num in nums:
  exist = False
  left = 0
  right = len(cards) - 1
  while left <= right:
    mid = (left + right) // 2
    if num == cards[mid]:
      exist = True
      break
    elif num < cards[mid]: right = mid - 1
    else: left = mid + 1
  if exist: print(1, end=' ')
  else: print(0, end=' ')
    
    
 #ii.
import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards_set = set(cards)
for num in nums:
  if num in cards_set: print(1, end = ' ')
  else: print(0, end = ' ')
    
    
'''
i. 이진 탐색
ii. 가지고 있는 cards 번호를 set으로 가지고 각 num마다 set
- ii가 더 
'''
