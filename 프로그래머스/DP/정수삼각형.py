'''
# L3. 정수 삼각형
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우의 최댓값?
아래 칸으로 이동할 때는 대각성 방향으로 한 칸 오른쪽/왼쪽으로만 이동 가능하다.
'''

def solution(triangle):               # dp = triangle 
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i - 1][j] if j < len(triangle[i]) - 1 else 0, triangle[i - 1][j - 1] if j >= 1 else 0)       # 왼쪽 위나 오른쪽 위의 수 중 더 큰 것 더함
    return max(triangle[-1])          # 삼각형의 마지막 줄에서 최댓값 출력
