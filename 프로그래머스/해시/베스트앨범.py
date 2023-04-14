'''
# L3. 베스트앨범
장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
노래는 고유 번호로 구분하며, 수록 기준은 다음과 같다.
1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록한다.
베스트 앨범에 수록된 곡 순서대로 고유 번호를 출력하시오.
'''

def solution(genres, plays):
    musics = dict()                                                   # 장르: [[고유 번호, 재생 수]..]
    musicIndex = dict()                                               # musicPlays에 대한 장르별 idx
    musicPlays = []                                                   # [[장르명, 장르 곡 전체 재생 수]...]
    for idx, genre in enumerate(genres):                              # musics, musicIndex, musicPlays 구성
        if genre not in musics.keys():
            musicIndex[genre] = len(musicPlays)
            musicPlays.append([genre, plays[idx]])
            musics[genre] = [[idx, plays[idx]]]
        else:
            musicPlays[musicIndex[genre]][1] += plays[idx]
            musics[genre].append([idx, plays[idx]])
    musicPlays.sort(key=lambda x:-x[1])                               # musicPlays로 1번 기준 충족
    for genre in musics:                                              # musics으로 각 장르 별 곡에 대해 2번 기준 충족
        musics[genre].sort(key=lambda x:-x[1])

    answer = []
    for [genre, cnt] in musicPlays:                                   # 장르별로 최대 2곡씩 수록 
        cnt = 0
        for element in musics[genre]:
            if cnt == 2: break
            answer.append(element[0])
            cnt += 1
    return answer
  
  
  '''
  고유 번호 순서대로 musics을 구성하고, sort할 때는 이를 유지하기 위해 reverse=True가 아닌 음수 키 값을 활용
  '''
