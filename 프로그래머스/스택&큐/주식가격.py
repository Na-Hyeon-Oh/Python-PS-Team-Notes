'''
# L2. 주식가격
초 단위의 주식가격이 담긴 배열 prices가 주어질 때,
각 초 기준으로 가격이 떨어지지 않은 기간을 return
'''

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
