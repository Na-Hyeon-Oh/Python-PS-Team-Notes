'''
# L2. 타켓 넘버
n개의 음이 아닌 정수가 주어질 때, 순서를 바꾸지 않고 적절히 더하거나 빼서 타켓 넘버를 만드는 경우의 수를 출력하시오.
'''

# i. dfs - ii. 보다 

global result
result = 0

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
        
    return result

def dfs(numbers, target, idx, cnt):
    global result
    if idx == len(numbers): 
        if cnt == target: result += 1
        return cnt

    dfs(numbers, target, idx + 1, cnt - numbers[idx])
    dfs(numbers, target, idx + 1, cnt + numbers[idx])
    return result
  
# ii. 재귀

def solution(numbers, target):
    if len(numbers) == 0 and target == 0: return 1
    elif len(numbers) == 0: return 0
    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])                  # - , +
