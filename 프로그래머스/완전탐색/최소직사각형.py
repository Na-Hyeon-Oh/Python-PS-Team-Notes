'''
# L1. 최소직사각형
4가지 명함의 가로, 세로 길이가 주어지고 명함을 가로로 눕혀 넣을 수 있다고 할 때, 
지갑의 최소 크기?
'''

def solution(sizes):
    answer = 0
    w, h = [], []
    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
        
    answer = max(w) * max(h)  
    return answer
