'''
# L1. K번째수
array에서 i부터 j번째 숫자까지 잘라 정렬했을 때 k번째에 있는 수 출력 
'''

def solution(array, commands):
    answer = []
    for [i, j, k] in commands:
        scope = array[i-1:j]
        scope.sort()
        answer.append(scope[k-1])
    return answer
