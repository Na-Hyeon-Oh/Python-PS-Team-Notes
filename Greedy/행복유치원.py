# 행복 유치원
# https://www.acmicpc.net/problem/13164
'''
N명의 원생들을 키 순서대로 줄 세우고 총 K조로 나누려고 한다.
각 조에서 티셔츠를 맞추는 비용은 
각 조에서 가장 키가 큰 원생과 가장 작은 원생의 키 차이만큼 든다고 할 때, 
티셔츠 비용의 합의 최솟값은?
* 1 <= N <= 300,000
* 시간 제한 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
heights = list(map(int, input().split()))

costs = []
for i in range(n):
  if i == 0: continue
  costs.append(heights[i] - heights[i - 1])
costs = sorted(costs)
minCost = sum(costs[0 : n - k])

print(minCost)
  
'''
최소 비용을 맞추기 위해서는 각 학생간 키 차이 중 최소값부터 n - k 개만 더해주면 된다
'''
