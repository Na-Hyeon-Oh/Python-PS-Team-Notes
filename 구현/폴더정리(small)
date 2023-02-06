# 폴더 정리 (small)
# https://www.acmicpc.net/problem/22860
'''
main 폴더의 하위 구조가 주어질 때, 주어지는 쿼리에 대해 폴더와 파일의 정보를 알려주는 프로그램
- 폴더 개수 N개(main 제외)와 파일의 개수 M개가 주어지고,
상위 폴더의 이름 P, 폴더 또는 파일의 이름 F, 폴더인지 아닌지 알려주는 C(1/0)가 공백으로 구분되어 주어진다.
* 1 <= N, M, Q <= 1,000, 1 <= P, F <= 10, 0 <= C <= 1
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
directoryFile = dict()
childDirectory = dict()
for _ in range(n + m):
  info = list(input().split())
  if info[2] == "1":  # folder
    if not info[1] in directoryFile:
      directoryFile[info[1]] = []  # dictinary에 해당 key가 있는지 확인
    if info[0] in childDirectory: childDirectory[info[0]].append(info[1])
    else: childDirectory[info[0]] = [info[1]]
  else:  # file
    if info[0] in directoryFile: directoryFile[info[0]].append(info[1])
    else: directoryFile[info[0]] = [info[1]]

q = int(input())
for _ in range(q):
  query = list(input().split('/'))
  files = []
  curDir = query[len(query) - 1]
  searchDir = [curDir]
  while searchDir:
    target = searchDir.pop(0)
    if target in childDirectory: searchDir.extend(childDirectory[target])
    if target in directoryFile: files.extend(directoryFile[target])
  print(len(set(files)), len(files))  # 중복 제거 -> set 이용

  
''' 
- input으로 주어진 값을 통해 각 폴더에 포함된 "파일"을 dictionary의 리스트로 저장
+ 각 폴더에 들어있는 하위 디렉토리 dictionary의 리스트로 저장
- query에서 주어진 마지막 폴더를 기준으로, 해당 폴더에 어떤 하위 폴더가 있는지 파악하여
마지막 폴더와 그 하위 폴더에 들어있는 모든 파일들을 구하고 개수와, 종류를 출력
'''
