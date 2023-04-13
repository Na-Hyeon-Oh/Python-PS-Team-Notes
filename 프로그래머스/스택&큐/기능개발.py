'''
# L2. 기능개발
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 progresses 정수 배열과,
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때,
각 배포마다 진도가 100%로 채워진 몇 개의 기능이 배포되는지 return
'''


def solution(progresses, speeds):
    answer = []
    remainDay = []
    for i in range(len(progresses)):
        target = - ((progresses[i] - 100) // speeds[i])                                     # math.ceil # 음수로 나눠 다시 양수로 바꾸기
        if not(len(remainDay) == 0 or (len(remainDay) > 0 and remainDay[0] >= target)):
            answer.append(len(remainDay))
            remainDay = []
        remainDay.append(target)
    if len(remainDay) > 0: answer.append(len(remainDay))
    return answer
  
 '''
 - math.ceil 대신 음수-양수 변환 활용
 - 걸리는 시간이 더 길면 그 전까지의 개수 answer에 
 '''
