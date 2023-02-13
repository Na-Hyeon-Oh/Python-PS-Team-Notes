# IF문 좀 대신 써줘
# https://www.acmicpc.net/problem/19637
'''
캐릭터의 전투력에 밪는 칭호를 출력하는 프로그램
* 1 <= N(칭호의 개수), M(캐릭터의 개수) <= 10^5
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
characterNames = []
characterPowers = []
for _ in range(n):
  name, power = input().split()
  characterNames.append(name)
  characterPowers.append(int(power))
for _ in range(m):
  target = int(input())

  result = 0  
  left = 0
  right = n - 1
  while left <= right:
    mid = (left + right) // 2  
    if target <= characterPowers[mid]: 
      result = mid
      right = mid - 1
    else: left = mid + 1
  print(characterNames[result])

    
'''

'''

