'''
# L3. 이중우선순위큐
I 숫자 -> 숫자를 큐에 삽입
D 1 -> 큐 최댓값 삭제
D -1 -> 큐 최솟값 삭제
위의 연산들을 수행하고 큐가 비어 있으면 [0, 0], 아니면 [최댓값, 최솟값]을 return하라.
'''

def solution(operations):
    answer = [0, 0]
    queue = []
    for cmd in operations:
        number = int(cmd[2:])
        if cmd.startswith("I "): queue.append(number)
        elif cmd.startswith("D "):
            if len(queue) > 0:
                if number > 0: queue.remove(max(queue))
                else: queue.remove(min(queue)) 
    if len(queue) > 0: answer = [max(queue), min(queue)]
    return answer
  
  
