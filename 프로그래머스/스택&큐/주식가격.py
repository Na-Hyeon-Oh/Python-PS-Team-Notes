'''
# L2. 주식가격
# Stack으로 다시 풀어보기
초 단위의 주식가격이 담긴 배열 prices가 주어질 때,
각 초 기준으로 가격이 떨어지지 않은 기간을 return
'''

# i. O(n^2)
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] <= prices[j]: 
                if j == len(prices) - 1: answer.append(cnt)
            else:
                answer.append(cnt)
                break
    answer.append(0)
    return answer


# ii. Stack 이용 O(n^2) but i보다 빠름 
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:             # 이후의 초에서 감소한 경우
            past, _ = stack.pop()
            answer[past] = i - past                                 # idx 차이 = 몇 초동안 가격이 떨어지지 않았는를 answer에 저장
        stack.append([i, prices[i]])
    for i, s in stack:                                              # 끝까지 감소하지 않은 경우
        answer[i] = len(prices) - 1 - i
    return answer
