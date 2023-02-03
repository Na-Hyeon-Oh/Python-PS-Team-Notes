# 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
'''
문자열 s가 주어질 때, 단어이면 뒤집어서 출력하라.
- <tag>인 경우는 단어가 아니다.
* s <= 100,000
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()
  
S = input()

words = []
word = ""
isTag = False
def tagAppend(target):
  words.append(target)
  word = ""
  isTag = False
def wordAppend(target):
  words.append(target[::-1])
  word = ""
  isTag = False

for s in S:
  if s == ' ' and isTag != True:
    words.append(word[::-1] + s)
    word = ""
    continue
  if isTag == True and s == '>': 
    words.append(word + s)
    word = ""
    isTag = False
    continue
  if s == '<': 
    if isTag == False and len(word) == 0: 
      word = s
      isTag = True
    elif isTag != True: 
      words.append(word[::-1])
      word = s
      isTag = True
    continue
  word += s
if len(word) > 0: words.append(word[::-1])

for word in words:
  print(word, end='')

'''

'''
