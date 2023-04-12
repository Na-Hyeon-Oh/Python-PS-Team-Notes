'''
# L2. H-Index
과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었을 때 h의 최댓값을 구하시오.
'''

# i. 내림차순 기준
def solution(citations):
    answer = len(citations)
    citations.sort(reverse = True)
    for idx, citate in enumerate(citations):
        if idx >= citate:
            return idx
    return answer
  
# ii. 오름차순 기준
def solution(citations):
    answer = 0
    citations.sort()
    for idx, citate in enumerate(citations):
        if len(citations) - idx <= citate:
            return len(citations) - idx
    return answer
  
  
'''
문제 이해가 어려웠당..
* enumerate(list) => (idx, list[idx]) 값을 얻을 수 있다.
'''
