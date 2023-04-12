'''
# L1. 완주하지 못한 선수
마라톤을 참가한 여러 선수가 있고, 한 명만 완주하지 못했을 때, 이 선수의 이름을 return 하시오
* 참가자 중에는 동명이인이 있을 수 있다.
'''

# i. naive한 방법 + 정렬
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant) - 1 or participant[i] != completion[i]:
            return participant[i]
          
## ii. 해시 이용
from collections import Counter
def solution(participant, completion):
  answer = Counter(participant) - Counter(completion)
  return list(answer.keys())[0]

'''
정렬 후 다른 순서일 경우 해당 참가자는 완주하지 못했다는 것이므로 출
'''
