'''
# L3. 네트워크
n개의 컴퓨터가 주어져 있고, 각 컴퓨터마다 연결정보가 0, 1로 주어져있을 때,
연결된 네트워크 개수 ?
'''

global visited
visited = []

def solution(n, computers):
    global visited
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i)
            answer += 1
    return answer

def dfs(n, computers, idx):
    global visited
    visited[idx] = True
    for i in range(n):
        if i == idx: continue
        if computers[idx][i] == 1 and not visited[i]: dfs(n, computers, i)
    
