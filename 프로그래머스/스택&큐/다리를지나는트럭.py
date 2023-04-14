'''
# L2. 다리를 지나는 트럭
# Queue
트럭 여러 대가 일차선 다리를 정해진 순으로 건널 때,
모든 트럭이 다리를 건너는데 최소 몇 초가 걸리는가?
다리에는 트럭이 최대 bridge-length대 만큼 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있다.
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge, truck_weights에 대한 queue 생성
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(t for t in truck_weights)
    answer = 0
    bridge_weight = 0
    while bridge:
        answer += 1                                     # 1초씩 증가
        bridge_weight -= bridge.popleft()           

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:        # 다음 트럭이 bridge_weight를 넘기지 않으면 다리에 진입
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:                                                 # 아니면 빈 도로 
                bridge.append(0)

    return answer
