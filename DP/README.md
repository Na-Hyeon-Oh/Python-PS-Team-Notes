# Dynamic Programming (동적 계획법)

- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
- 이미 계산된 결과(SubProblem)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함

- 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제되는 경우가 많다.

## Condition

1. Optimal Substructure (최적 부분 구조)
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
3. Overlapping Subproblem (중복되는 부분 문제)
    - 동일한 작은 문제를 반복적으로 해결하여야 한다.

## Solution

* Memoization
    - 한 번 계산한 결과를 메모리 공간에 메모하는 기법
    - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴 (Cashing)

1. Top-down(하향식)
    - 재귀적

2. Bottom-up(상향식)
    - 반복문과 결과 저장용 리스트는 DP 테이블이라 부름
    - DP의 전형적인 형


## EX

- 피보나치 수열
    1. 재귀 함수 -> f(k)가 여러 번 호출됨 (중복되는 부분 문제)
        - 시간복잡도 : O(2^N)
       
        ![image](https://user-images.githubusercontent.com/64342804/222308573-15f6a338-47a7-4890-b243-91e3295d152d.png)

    2. DP
        - 시간복잡도 : O(N)
        ```
        # Top-down
        dp = [0] * 100
      
        def fibo(x):
          if x == 1 or x == 2: return 1
          if d[x] != 0: return d[x]
          d[x] = fibo(x - 1) + fibo(x - 2)
          return d[x]
      
        print(fibo(99))
      
        # Bottom-up
        dp = [0] * 100
        dp[1] = 1
        dp[2] = 1
        n = 99
      
        for i in range(3, n + 1):
          d[i] = d[i-1] + d[i-2]
      
        print(d[n])
        ```

- 개미 전사

    - 일직선으로 이어진 여러 식량창고(3 <= N <= 100)를 몰래 공격하여 약탈하려 할 때, 들키지 않기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
    - 약탈한 식량의 최댓값?
    - 시간제한 1초, 메모리제한 128MB
        
        ```
        n = int(input())
        k = list(map(int, input().split()))

        dp = [0] * n        # dp[i] : i까지의 범위에서 각 식량창고에서 약탈한 식량의 최댓값
        for i in range(n):
            if i > 1: dp[i] = max(dp[i - 1], dp[i - 2] + k[i])
            else: dp[i] = k[i]

        print(dp[n - 1])
        ```

- 1로 만들기

    - 정수 X (1<= X <= 30,000)가 주어졌을 때 할 수 있는 연산은 다음과 같이 4가지이다.
            - X가 5로 나누어 떨어지면, 5로 나누기
            - X가 3으로 나누어 떨어지면, 3으로 나누기
            - X가 2로 나누어 떨어지면, 2로 나누기
            - X에서 1을 뺀다.
    - X를 1로 만들고자 할 때, 연산을 사용하는 횟수의 최솟값?
    - 시간제한 1초, 메모리제한 128MB
    - 비슷한 유형의 백준 문제 : https://www.acmicpc.net/problem/1463
    
        ```
        x = int(input())
        bigNum = 1e5

        dp = [0] * x
        for i in range(1, x):
            target = i + 1
        dp[i] = min((dp[target // 5 - 1] if target % 5 == 0 else bigNum),
                    (dp[target // 3 - 1] if target % 3 == 0 else bigNum), 
                    (dp[target // 2 - 1] if target % 2 == 0 else bigNum), 
                    dp[i - 1]) + 1

        print(dp[x - 1])
        ```
        - Greedy로 풀기에는 5로 나누었을 때 항상 가장 최소의 연산 횟수를 도출하지 않는다.

- 효율적인 화폐 구성

    - N가지 (1 <= N <= 100) 종류의 화폐가 있을 때 화폐의 개수를 최소한으로 이용해 그 가치의 합이 M원 (1 <= M <= 10,000) 이 되도록 하려 한다.
    - 각 종류의 화폐의 사용에는 제한이 없을 때
    - M원을 만들기 위한 최소한의 화폐 개수? (불가능할 때는 -1 출력)
    - 시간제한 1초, 메모리제한 128MB
            
            ```
            n, m = map(int, input().split())
            money = list(int(input()) for _ in range(n))

            dp = [-1] * (m + 1)                 # dp[i]: i원을 만들기 위한 최소 화폐 개수
            for value in money:
                if value <= m: dp[value] = 1
            for i in range(1, m + 1):
                minValue = 1e5
                for value in money:
                    if i - value >= 0 and dp[i - value] != -1: minValue = min(minValue, dp[i - value] + 1)
                if minValue != 1e5: dp[i] = minValue

            print(dp[m])
            ```

- 금광
    
    - N * M (1 <= N, M <= 20) 크기의 금광이 있고, 각 칸에는 매장된 금의 개수(1 <= 금의 개수 <= 100)가 있다.
    - 처음에 첫 번째 열의 어느 행에서든 출발할 수 있을 때, M - 1번에 걸쳐 오른쪽 위/오른쪽/오른쪽 아래 중 하나의 위치로 이동하여 채굴자가 얻을 수 있는 금의 최대 크기는?
    - 1 <= T (테스트케이스 개수) <= 1000
    - 시간제한 1초, 메모리제한 128MB
    
            ```
            t = int(input())
            for _ in range(t):
            n, m = map(int, input().split())
            gold = list(map(int, input().split()))
            dp = []
            for i in range(n):
              dp.append(gold[i * m: (i + 1) * m])               # gold를 m개씩 split
              #row = []
              #for j in range(m):
              #  row.append(gold1d[i * m + j])
              #  if j % m == m - 1: gold2d.append(row)

            for j in range(1, m):
              for i in range(n):
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0, dp[i + 1][j - 1] if i + 1 < n and j - 1 >= 0 else 0, dp[i][j - 1] if j - 1 >= 0 else 0)

            result = 0
            for i in range(n):
              result = max(result, dp[i][m - 1])
            print(result)
            ```
            - 금광의 모든 위치에서 왼쪽 위에서 오는 경우, 왼쪽 아래에서 오는 경우, 왼쪽에서 오는 경우를 고려
            - m - 1번 오른쪽으로 이동하므로 마지막 위치는 m - 1열
    
- 병사 배치하기

    - 각 전투력 (<= 10,000,000) 을 보유한 N명 (1 <= N <= 2,000) 의 병사가 무작위 나열되어 있을 때, 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하고자 한다.
    - 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수?
    - 시간제한 1초, 메모리제한 256MB
    - 비슷한 유형의 백준 문제 : https://www.acmicpc.net/problem/11053
            
            ```
            n = int(input())
            power = list(map(int, input().split()))

            power.reverse()            # LIS 문제로 변환
            dp = [1] * n
            for i in range(1, n):
                for j in range(0, i):
                    if power[i] > popwer[j]: dp[i] = max(dp[i], dp[j] + 1)

            print(n - max(dp))
            ```
            
            - Longest Increasing Subsequence (LIS) : 가장 긴 증가하는 부분 수열
                - D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
                - 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
                - i * j => 최악의 경우 시간 복잡도 : O(n^2)
            - 가장 긴 감소하는 부분 수열을 찾는 문제 -> LIS 알고리즘을 반대로 수행 by power를 reverse
            

## DP VS 분할 정복

- 공통점 : 모두 최적 부분 구조를 가질 때 (큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황일 때) 사용할 수 있다.
    
- 차이점 : 부분 문제의 중복 여부
    - DP : 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
    - 분할 정복 : 동일한 부분 문제가 반복적으로 계산되지 않는다.
            
            Ex. 퀵정렬
                 - 한번 기준 원소인 Pivot이 자리를 변경해서 자리를 잡으면 (Divide 시점) 그 기준 원소의 위치는 바뀌지 않음
                 
     
