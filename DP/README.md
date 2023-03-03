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



## DP VS 분할 정복

- 공통점 : 모두 최적 부분 구조를 가질 때 (큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황일 때) 사용할 수 있다.
    
- 차이점 : 부분 문제의 중복 여부
    - DP : 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
    - 분할 정복 : 동일한 부분 문제가 반복적으로 계산되지 않는다.
            
            Ex. 퀵정렬
                 - 한번 기준 원소인 Pivot이 자리를 변경해서 자리를 잡으면 (Divide 시점) 그 기준 원소의 위치는 바뀌지 않음
                 
     
