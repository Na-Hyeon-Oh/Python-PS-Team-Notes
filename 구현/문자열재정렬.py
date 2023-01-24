# 문자열 재정렬
'''
알파벳 대문자, 숫자(0~9)로만 이루어진 문자열이 입력으로 주어질 때,
모든 알파벳은 오름차순으로 정렬하여 출력한 뒤에, 숫자를 모두 더한 값을 이어서 출력하기
'''

s = input()

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
strList = []
numCount = 0
for i in s:
  if i in nums: numCount += int(i)
  else: strList.append(i)
strList.sort()
string = ''.join(strList)        # 리스트를 정렬한 것을 string으로 붙이기

if numCount != 0: print(f'{string}{numCount}')
else: print(string)
  
'''
* str type 정렬은 X, list로 정렬하여 str로 변환
'''
