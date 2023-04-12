'''
* 다시 풀어보기
# L2. 가장 큰 수
0 이상 1000 이하의 원소를 가진 numbers 리스트가 주어질 때, 해당 정수를 모두 이어 붙여 만들 수 있는 가장 큰 수를 출력하라.
'''

# i. 
def solution(numbers):
    numbers = list(map(str, numbers))                               # int list -> str list
    numbers.sort(key=lambda x: x * 3, reverse=True)                 # 최소 세자리 수로 맞추기
    return str(int(''.join(numbers)))

'''
각 원소는 최대 4자리 자릿수이므로, 30, 3과 같은 경우 3 > 30의 우선순위를 갖게 해주기 위해 자릿수를 그 이상으로 맞춰준 것을 key로 내림차순 sort한다.
'''
  
# ii. key function 활용하기
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

'''
functools 라이브러리를 활용해 key function을 넘겨 준다.
key function에서는 a, b의 숫자가 있을 때 각 숫자의 순서에 따라 어떤 값이 더 큰지에 따라 다른 결과를 반환한다. 
'''
