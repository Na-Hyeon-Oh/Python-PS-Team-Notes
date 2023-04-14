'''
# L3. 등굣길
집(1, 1)에서 학교(m, n)까지 가는 길은 m * n 크기의 격자 모양으로 나타내며 
물에 잠기지 않은 지역을 통해 학교를 가려 할 때,
최단 경로의 개수를 1,000,000,007로 나눈 나머지를 구하시오
'''

# 아래쪽, 오른쪽 => 로만 움직이므로 모든 가능한 경로가 최단 경로 
dx = [0, 1]
dy = [1, 0]

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]    # (i, j) 까지의 최단경로 개수
    dp[0][0] = 1
    for [x, y] in puddles:              # 침수 지역
        dp[y - 1][x - 1] = -1
    
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or dp[i][j] == -1: continue
            for k in range(2):
                nx, ny = j - dx[k], i - dy[k]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and dp[ny][nx] != -1:
                    dp[i][j] += dp[ny][nx]
    
    return dp[n - 1][m - 1] % 1000000007
