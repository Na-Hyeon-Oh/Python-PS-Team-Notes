'''
# L2. 모음 사전
'A', 'E', 'I', 'O', 'U'만을 이용하여 만들 수 있는 길이 5이하의 모든 단어가 수록된 사전이 있을 때,
어떠한 단어가 해당 사전에서 몇 번 째 단어인지 return 하시오
'''

from itertools import product
def solution(word):
    # alphabets 이용해 dictionary 생성
    alphabets = ["A", "E", "I", "O", "U"]
    dictionary = []
    for i in range(5):
        dictionary.extend(map("".join, product(alphabets, repeat=i + 1)))
    dictionary.sort()
    
    # 몇 번째에 있는지 찾기
    answer = dictionary.index(word) + 1
    return answer
  
  '''
  1~5 길이의 중복순열을 활용해 해당 dictionary를 구성하고 정렬하여 
  list 상 몇 번째에 위치해있는지 출력 
  '''
