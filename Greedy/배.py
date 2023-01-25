# 배
# https://www.acmicpc.net/problem/1092
'''
크레인이 N대 있고, 각 크레인은 무게 제한이 있다.
전체 박스는 M개이고, 박스는 1분에 하나씩 배에 실을 수 있다.
모든 박스를 배로 옮기는데 드는 시간의 최솟값?
* 1 <= N <= 50, 1 <= M <= 10,000,
(각 크레인 무게 제한), (각 박스 무게) <= 1,000,000
* 시간 제한 2초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
craneLimits = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxWeights = sorted(list(map(int, input().split())), reverse=True)

result = 0
if boxWeights[0] > craneLimits[0]: 
  print(-1)
  sys.exit()
while boxWeights:
  if not boxWeights:
    break
  for crane in craneLimits:
    for box in boxWeights:
      if crane >= box:
        boxWeights.remove(box)
        break
  result += 1
      
print(result)


'''
* Python3가 아닌 PyPy3로 해야 시간 초과 안남
가장 큰 크레인 무게 제한 기준으로 큰 박스부터 검사하며 이동시킨다.
* for 문을 도는 동안 해당 for문의 range list를 remove하면 오류가 증가할 확률 높으므로 반드시 break 사용하기
'''
