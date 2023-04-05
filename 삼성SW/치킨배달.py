# [CT_G5] 치킨 배달
# https://www.acmicpc.net/problem/15686
'''
N * N (2 <= N <= 50) 도시에 빈 칸, 치킨집, 집(0, 2, 1) 중 하나가 각 칸마다 존재한다.
각 집과 가장 가까운 치킨집 사이의 거리(|r1 - r2| + |c1 - c2|)는 치킨 거리이며,
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
치킨 집 중 최대 M개 (1 <= M <= 13)를 고르고 나머지 치킨집은 모두 폐업시킬 때, 도시의 치킨 거리가 가장 작게 되는 프로그램을 작성하시오.
* 시간 제한 1초
* 메모리 제한 512MB
'''

def combination(arr, r):              # 재귀 활용
    result = []
    if r > len(arr): return result
    if r == 1:
        for element in arr:
            result.append([element])
    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in combination(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)
    return result

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# 각 집과 치킨집 위치 저장
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1: homes.append([i, j])
        elif city[i][j] == 2: chickens.append([i, j])

# 치킨집 최대 M개 선택 조합
candidates = combination(chickens, m)
# 각 치킨집 조합별로 최소 도시 치킨거리 구하기
result = 1e8
for candidate in candidates:
    cityChickenStreet = 0
    for r1, c1 in homes:
        chickenStreet = 1e8
        for r2, c2 in candidate:
            chickenStreet = min(distance(r1, c1, r2, c2), chickenStreet)
        cityChickenStreet += chickenStreet
    result = min(cityChickenStreet, result)

print(result)

'''
N과 M의 범위가 100 이하로 작음 -> 완전 탐색 가능
- 치킨집을 최대 m개 선택했을 때 도시 치킨 거리가 최소가 된다. 따라서 m개에 대한 조합만 고려해도 된다.

'''
