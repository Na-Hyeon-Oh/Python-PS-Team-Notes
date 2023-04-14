'''
# L3. 여행경로
ICN 공항에서 주어진 항공권을 모두 이용하여 여행경로를 짜려 한다.
방문 공항 경로를 RETURN 하시오.
* 가능한 경로가 2개 이상일 경우, 알파벳 순서가 앞서는 경로를 return
* 모든 도시를 방문할 수 없는 경우는 없다.
'''

# i. global 
from copy import deepcopy

global answer
answer = []

def solution(tickets):
    # 출발-도착 cities dictionary 만들기 -> 오름차순 정렬 
    cities = dict()
    for [src, dest] in tickets:
        cities[src] = cities.get(src, [])
        cities[src].append(dest)
    for city in cities:   
        cities[city].sort()

    dfs(len(tickets) + 1, ["ICN"], cities)      # dfs 이용 경로 탐색                   
    return answer[0]

def dfs(n, arr, cities):
    if len(answer) >= 1: return
    if len(arr) == n: answer.append(arr)
    src = arr[-1]
    for dest in cities.get(src, []):
        tmpCities = deepcopy(cities)
        tmpCities[src].remove(dest)
        dfs(n, arr + [dest], tmpCities)
        
        
# ii. global 쓰지 않고 성능 개선

from collections import defaultdict 

def dfs(graph, N, key, footprint):
    if len(footprint) == N + 1: return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret: return ret

def solution(tickets):
    graph = defaultdict(list)
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for node in graph:
        graph[node].sort()

    return dfs(graph, N, "ICN", ["ICN"])
