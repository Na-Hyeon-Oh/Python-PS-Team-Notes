'''
# L2. 더 맵게
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해,
스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 섞어 새로운 음식을 만든다.
그 결과 이를 위해 새로운 음식을 만드는 최소 횟수를 출력하시오.
* 만들 수 없는 경우 -1 return
'''

from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1: return -1
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a + b * 2)
        answer += 1
    return answer
