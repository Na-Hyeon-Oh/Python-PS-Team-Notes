'''
# L2. 피로도
각 던전을 탐험하기 위한 최소 피로도와 탐험을 했을 때 소모 피로도가 주어지고, 현재 유저에게 남은 피로도가 주어진다.
유저가 탐험할 수 있는 최대 던전 수?
'''


from itertools import permutations

def solution(k, dungeons):
    answer = -1
    cases = permutations(dungeons, len(dungeons))
    for element in cases:
        currentK = k
        cnt = 0
        for [a, b] in element:
            if currentK >= a:
                currentK -= b
                cnt += 1
            else: break
        answer = max(cnt, answer)
    return answer
  
  
  '''
  각 던전을 탐험하는 순서에 대한 경우를 permutation으로 뽑은 뒤,
  각 경우를 탐색해 가장 많은 던전을 탐색할 수 있는 경우 출력 
  '''
