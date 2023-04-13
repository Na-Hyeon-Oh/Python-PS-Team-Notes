'''
# L2. 프린터
# Queue
중요도가 높은 문서를 먼저 인쇄하는 프린터가 있을 때 다음과 같이 인쇄 작업을 수행한다.
1. 인쇄 대기 목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄한다.
인쇄를 요청한 문서가 몇 번째로 인쇄되는지를 출력
* 숫자가 클수록 중요도가 높음
'''

from collections import deque

def solution(priorities, location):
    q = deque()
    for e in priorities:
        q.append(e)
        
    answer = 1
    while True:
        maxP = max(q)
        e = q.popleft()
        if location == 0:                   # 요청한 문서일 경우
            if e < maxP:                    # 우선순위가 더 높은 인쇄물이 있는 경우
                q.append(e)
                location = len(q) - 1
            else: return answer             # 우선순위가 제일 높을 때
        else:                               # 요청할 문서가 아닐 경우
            location -= 1
            if e < maxP: q.append(e)        # 우선순위가 더 높은 인쇄물이 있는 경우
            else: answer += 1               # 우선순위가 제일 높을 
    return answer
