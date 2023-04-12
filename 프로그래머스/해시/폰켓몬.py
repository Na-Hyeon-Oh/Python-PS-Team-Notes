'''
# L1. 폰켓몬
연구실에 있는 N마리의 폰켓몬 중 N/2마리를 가져가도 될 때 가장 다양한 종류의 폰켓몬을 가져가려 할 때,
폰켓몬 종류 번호의 개수를 return 하시오.
'''

def solution(nums):
    answer = 0
    maxTypeLength = len(set(nums))
    selectNo = len(nums) // 2
    if maxTypeLength <= selectNo: answer = maxTypeLength          # n / 2가 종류보다 많거나 같기만 하면 항상 최대 
    else: answer = answer = selectNo 
    return answer
  
