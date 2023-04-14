'''
# L3. 단어 변환
단어 begin이 words의 변환 과정을 거쳐 target이 되기 위해 가장 짧은 변환 과정의 길이는?
* 한 번에 한 개의 알파벳만 바꿀 수 있다.
'''

from copy import deepcopy

global answer
answer = 1e5

def solution(begin, target, words):
    return answer if dfs(begin, target, words, 0) != 0 else 0

def dfs(begin, target, words, nth):
    global answer
    if begin == target: answer = min(answer, nth)                   # 가장 짧은 경우의 변환 개수 저장
    if target not in words or not words: return 0                   # 해당 경우는 변환이 안되거나 변환을 마저 진행할 수 없다.
    # 1개의 문자만 다른 경우
    convert = []
    for word in words:
        cnt = 0
        for i in range(len(begin)):
            if begin[i] != word[i]: cnt += 1
        if cnt == 1: convert.append(word)
    for word in convert:
        nextWords = deepcopy(words)
        nextWords.remove(word)                                      # 방문한 문자 빼기
        dfs(word, target, nextWords, nth + 1)                       
