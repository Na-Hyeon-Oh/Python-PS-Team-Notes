# ZOAC
# https://www.acmicpc.net/problem/16719
'''
ZOAC 게임을 새로운 규칙으로 진행하고자 한다.
정답인 문자열의 문자를 하나씩 보여주고자 할 때, 아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는 것이다.
* 제한 시간 1초
'''


s = list(input().rstrip())

result = [''] * len(s)

def zoac(arr, start):
  if not arr: return
  idx = arr.index(min(arr))
  result[start + idx] = min(arr)
  print(''.join(result))
  zoac(arr[idx + 1:], start + idx + 1)
  zoac(arr[:idx], start)

zoac(s, 0)

'''
- 재귀 활용 문제
- 가장 작은 Alphabet이 정해지면 해당 alphabet을 포함하여 그 뒤에 있는 문자열을 우선 탐색해야 함
'''
