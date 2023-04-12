'''
# L2. 소수 찾기
한자리 숫자가 적힌 종이 조각이 이어진 문자열이 주어질 때,
종이조각으로 만들 수 있는 소수가 몇 개인가?
'''

# i. 
from itertools import permutations

def solution(numbers):
    answer = 0
    numberList = list(numbers)                      # 각 숫자 쪼갠 list
    
    # permutation
    p = []
    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numberList, i))
    # permutation 결과로 number 만들기
    numbers = []
    for element in p:
        tmp = ""
        for i in range(len(element)):
            tmp += element[i]
        numbers.append(int(tmp))
    numbers = list(set(numbers))                    # 중복 제거
    
    # 소수 세기
    for element in numbers:
        answer += isSosu(element)
    return answer

def isSosu(candidate):
    if candidate <= 1: return 0	
    for i in range(2, candidate):
        if candidate % i == 0: return 0
    return 1

# ii. set의 합집합 활용
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
  
'''
중복을 없애기 위해 set 성질 활용
모든 순서 및 뽑는 를 고려하기 위해 permutation 활용
'''
