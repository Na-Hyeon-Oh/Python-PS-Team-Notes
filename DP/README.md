# Dynamic Programming (동적 계획법)

- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
- 이미 계산된 결과(SubProblem)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함

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
