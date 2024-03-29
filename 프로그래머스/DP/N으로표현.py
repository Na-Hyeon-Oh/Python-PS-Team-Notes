'''
# L3. N으로 표현
숫자 N과 사칙연산만 사용해서 number를 표현할 수 있을 때,
N 사용횟수의 최솟값을 return
* 그 값이 8보다 크면 -1 return
'''

def solution(N, number):
    sets = []
    for cnt in range(1, 9):                     # 1개부터 8개의 경우를 쓸 경우
       currentSet = set()
        currentSet.add(int(str(N) * cnt))       # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1):                # cnt만큼을 이용한 경우는 i개와 cnt - i개를 이용하는 경우를 조합하여 생성됨을 이용해 (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in sets[i]:
                for op2 in sets[-i - 1]:
                    currentSet.add(op1 + op2)
                    currentSet.add(op1 - op2)
                    currentSet.add(op1 * op2)
                    if op2 != 0: currentSet.add(op1 / op2)
        if number in currentSet: return cnt     # 만든 집합에 number가 처음(가장 작은 cnt) 나오는지 확인
        sets.append(currentSet)
    return -1

'''
ref. https://alreadyusedadress.tistory.com/115
'''
