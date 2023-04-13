'''
* 다시 풀어보기
# L2. 위장
스파이가 하루에 최소 하나의 의상을 입을 때, 서로 다른 옷의 조합의 수?
'''

def solution(clothes):
    clothDict = dict()
    for [name, cType] in clothes:
        clothDict[cType] = clothDict.get(cType, 0) + 1              # dict.get(key, initial) 있으면 get 없으면 0 반환
    
    # 모든 조합 (안 입는 경우 포함)
    answer = 1
    for cType in clothDict:
        answer *= (clothDict[cType] + 1)
    answer -= 1                             # 아무것도 입지 않는 경우 제외
    return answer

'''
# 테케 1에서 시간 초과
from itertools import combinations

def solution(clothes):
    clothDict = dict()
    for [name, cType] in clothes:
        if cType not in clothDict.keys(): clothDict[cType] = 1
        else: clothDict[cType] += 1
    keys = clothDict.keys()
    c = []
    for i in range(1, len(keys) + 1):
        c.extend(list(combinations(keys, i)))
    answer = 0
    for i in c:
        tmp = 1
        for element in i:
            tmp *= clothDict[element]
        answer += tmp
    
    return answer
'''
