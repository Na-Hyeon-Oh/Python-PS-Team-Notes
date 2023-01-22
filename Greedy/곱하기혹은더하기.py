# 곱하기 혹은 더하기
'''
0~9의 숫자로 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 모든 숫자 사이에 * / + 연산자를 넣고,
모든 연산을 왼쪽에서부터 순서대로 할 때
만들어질 수 있는 가장 큰 수를 구하는 프로그램
'''

data = input()

result = int(data[0])

for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)


'''
기본적으로 두 값을 곱하는 것이 더하는 것보다 더 큰 수를 만든다.
cf. 둘 중 하나의 수가 0, 1인 경우
'''
