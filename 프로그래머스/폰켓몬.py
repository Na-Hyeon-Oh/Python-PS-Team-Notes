def solution(nums):
    answer = 0
    maxTypeLength = len(set(nums))
    selectNo = len(nums) // 2
    if maxTypeLength <= selectNo: answer = maxTypeLength
    else: answer = answer = selectNo 
    return answer
