'''
# L1. 모의고사
1번, 2번, 3번 수포자가 찍는 방식이 각각 다음과 같을 때,
1번부터 마지막 문제까지의 정답이 순서대로 주어질 때 가장 많이 맞힌 사람을 오름차순으로 출력하시오.
'''

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l1, l2, l3 = len(first), len(second), len(third)
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i % l1]: cnt1 += 1
        if answers[i] == second[i % l2]: cnt2 += 1
        if answers[i] == third[i % l3]: cnt3 += 1
    
    maxScore = max(cnt1, cnt2, cnt3)
    if maxScore == cnt1: answer.append(1)
    if maxScore == cnt2: answer.append(2)
    if maxScore == cnt3: answer.append(3)
    answer.sort()                   # 오름차순
    return answer
