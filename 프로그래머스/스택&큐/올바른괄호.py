'''
# L2. 올바른 괄호
# stack
() 괄호가 올바로 짝지어서 주어진 경우 True를 리턴
'''

def solution(s):
    answer = True
    
    stack = []
    for e in s:
        if e == '(': stack.append(1)
        else:
            if len(stack) == 0: return False
            else: stack.pop()
    if len(stack) > 0: return False
    return True
