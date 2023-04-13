'''
# L1. 같은 숫자는 싫어
# 스택
배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있고, 연속해서 나타나는 숫자는 하나만 남기고 전부 제거하려고 한다.
순서는 유지하려 할 때 그 결과를 출력하시오.
'''

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0 or (len(answer) > 0 and answer[-1] != arr[i]):
            answer.append(arr[i])
    return answer
