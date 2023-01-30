# 택배
# https://www.acmicpc.net/problem/8980
'''
N개의 마을이 있고, 트럭이 있는 본부는 마을의 가장 왼쪽 끝에 있다.
마을의 개수(N), 트럭의 용량(C), 박스 정보(M; 보내는 마을번호, 받는 마을번호, 박스 개수)가 주어질 때, 다음 조건을 만족하면서 트럭 한 대로 배송할 수 있는 최대 박스 수를 구하시오.
1. 박스를 실으면, 박스는 받는 마을에서만 내린다.
2. 트럭은 지나온 마을로 되돌아가지 않는다
3. 박스들 중 일부만 배송할 수도 있다.
* 2 <= N <= 2,000, 1 <= C <= 10,000, 1 <= M <= 10,000
* 시간 제한 1초
'''

import sys

def input():
  return sys.stdin.readline()

n, c = map(int, input().split())
m = int(input())
mList = [list(map(int, input().split())) for _ in range(m)]
mList.sort(key=lambda mList:mList[1])

result = 0
capacity = [c for _ in range(n - 1)]
for i in range(m):
  valid = mList[i][2]
  for j in range(mList[i][0] - 1, mList[i][1] - 1): valid = min(valid, capacity[j])
  if valid > 0:
    for j in range(mList[i][0] - 1, mList[i][1] - 1): capacity[j] -= valid
    result += valid

print(result)

'''
- 조건 1번 때문에 받는 마을이 작을 수록(시작 마을과 끝 마을의 차이가 적을 수록이 아니다) 트럭에 더 많은 여유를 줄 수 있다.
 한번 방문한 도시를 다시 방문하지 않고 1번 도시부터 출발하기 때문에 1번 도시와 가까운 순으로 박스를 옮기는 것이 최적이다.
 ex. 2 3 50 / 1 3 50이 있고 c = 50일 때, 둘 중 하나만 옮길 수 있으므로, 시작 위치가 중요하지 
 - list.sort()와 sorted(list)의 차이: 선자는 list 자체를 오름차순 정렬하고, 후자는 list를 오름차순 정렬한 결과를 반환한다.
'''
