'''
# L2. 카펫
카펫의 패턴은 노란색 정사각형으로 이루어진 사각형 바깥으로 한 줄의 갈색의 정사각형이 있을 때,
노란색과 갈색으로 색칠된 각 격자의 개수를 통해 전체 카펫의 가로, 세로 크기를 출력하시오
* 가로 >= 세로
'''

def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0: 
            yw, yh = yellow // i, i
            if 2 * (yw + yh) + 4 == brown: return [yw + 2, yh + 2] 

'''
def solution(brown, yellow):
    candidates = []                                                 # 가능한 yellow의 [가로, 세로]
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0: candidates.append([yellow // i, i])
    
    answer = []
    for c in candidates:
        neededBrown = 2 * (c[0] + c[1]) + 4
        if neededBrown == brown: 
            answer = [c[0] + 2, c[1] + 2] 
            break
    return answer
'''
