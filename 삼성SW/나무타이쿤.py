'''
[CT_G5] 나무타이쿤
- 시뮬레이션 
'''

from copy import deepcopy

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
rules = [list(map(int, input().split())) for _ in range(m)]
global ingredients
ingredients = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(n, d, p):
    for i in range(len(ingredients)):
        x, y = ingredients[i]
        nx = (x + dx[d] * p) % n
        ny = (y + dy[d] * p) % n
        ingredients[i] = (nx, ny)

def grow(n):
    for x, y in ingredients:
        graph[x][y] += 1

    tmp = []
    for x, y in ingredients:
        cnt = 0
        if inRange(x - 1, y - 1) and graph[x - 1][y - 1] >= 1: cnt += 1
        if inRange(x - 1, y + 1) and graph[x - 1][y + 1] >= 1: cnt += 1
        if inRange(x + 1, y - 1) and graph[x + 1][y - 1] >= 1: cnt += 1
        if inRange(x + 1, y + 1) and graph[x + 1][y + 1] >= 1: cnt += 1
        tmp.append((x, y, cnt))
    for x, y, cnt in tmp:
        graph[x][y] += cnt

def removeAndSetIngredients(n):
    global ingredients
    nextIngredients = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2:
                exist = False
                for x, y in ingredients:
                    if x == i and y == j: 
                        exist = True
                        break
                if not exist: 
                    graph[i][j] -= 2
                    nextIngredients.append((i, j))
    ingredients = deepcopy(nextIngredients)

for rule in rules:              # simulate
    d, p = rule[0] - 1, rule[1]
    move(n, d, p)
    grow(n)
    removeAndSetIngredients(n)

result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

print(result)
