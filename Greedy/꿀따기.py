# 꿀 따기
# https://www.acmicpc.net/problem/21758
'''
N개의 장소가 있고, 두 마리의 벌이 서로 다른 장소에 위치한다.
또 다른 한 장소에는 벌통이 있는데, 각 벌이 시작한 장소를 제외하고 벌통까지 가는데 얻은 꿀의 양의 최대 총합을 구하라.
* 3 <= N <= 100,000
1 <= (각 장소의 꿀의 양) <= 10,000
* 시간 제한 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
list = list(map(int, input().split()))

result = 0
prefixSum = []
for i in range(n):
  if i == 0: prefixSum.append(list[0])
  else: prefixSum.append(prefixSum[i - 1] + list[i])

# Case1: 꿀통이 왼쪽 끝 -> 벌1의 위치 오른쪽 끝으로 고정
for i in range(1, n - 1):
  result = max(result, prefixSum[n - 2] - list[i] + prefixSum[i - 1])
# Case2: 꿀통이 오른쪽 끝 -> 벌1의 위치 왼쪽 끝으로 고정
for i  in range(1, n - 1):
  result = max(result, prefixSum[n - 1] - list[0] + prefixSum[n - 1] - prefixSum[i] - list[i])
# Case3: 꿀통이 가운데 -> 벌의 위치는 양 끝으로 고정, 벌통의 위치만 탐색
for i in range(1, n - 1):
  result = max(result, prefixSum[n - 2] - list[0] + list[i])
      
print(result)


'''
- 누적합
- a = max(a,b)로 최댓값 업데이트
'''
