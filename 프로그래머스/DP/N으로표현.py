'''
# L3. N으로 표현
숫자 N과 사칙연산만 사용해서 number를 표현할 수 있을 때,
N 사용횟수의 최솟값을 return
* 그 값이 8보다 크면 -1 return
'''

def solution(N, number):
    set_list = []
    for cnt in range(1, 9):                 # 1개부터 8개의 경우를 쓸 경우
        partial_set = set()
        partial_set.add(int(str(N) * cnt))  # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1):            # cnt만큼을 이용한 경우는 i개와 cnt - i개를 이용하는 경우를 조합하여 생성됨을 이용해 (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 집합에 number가 처음(가장 작은 수) 나오는지 확인
        if number in partial_set: return cnt
        set_list.append(partial_set)
    return -1
