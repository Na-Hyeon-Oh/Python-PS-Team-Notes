# Greedy Algorithm

- Locally(현재) 최적의 선택이면 Globally하게도 최적의 선택일 거라는 믿음에서 최적해를 구하는 근사적인 방법

- 현재 상황에서 가장 좋은 선택을 하는 방법

- NOT ALWAYS TRUE (NO GUARANTEE)  *BUT* useful

## Condition

1. greedy choice property

      : 앞의 선택이 이후의 선택에 영향이 X

2. optimal substructure

      : 전체 문제에 대한 Optimal 해가 sub-problem에 대해서도 optimal

:arrow_right: 만족 시, '매트로이드' 구조의 문제

:arrow_right: 만족하지 않더라도, 엄밀한 증명 이후 탐욕 알고리즘을 Approximation Algorithm(*)으로 사용 가능

* Approximation Algorithm : 최적화된 답은 아니더라도 빠르게 어느 정도 보장된 근사값을 구할 수 있음

## 알고리즘 문제 Solution

0. 해당 문제가 그리디 알고리즘 문제인지 판단하고 그렇게 판단했다면 정당성을 입증할 수 있는 근거를 파악하여야 함  :star:

1. Selection Procedure

      : 현재 상태에서의 가장 optimal한 정답 선택

2. Feasibility Check

      : 해당 정답이 문제 조건을 만족하는지 검사

3. Solution Check
 
      : 문제 해결되었는지 검사, or 1번으로 돌아가기

## Ex

1. 거스름돈 최소한의 동전 개수로 거슬러주기

```
n = 1260
count = 0

coinArr = [500, 100, 50, 10]      # 큰 단위의 화폐부터 차례대로 확인하기

for coin in coinArr:
    count += n // coin            # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin

print(count)
```

:star: 큰 화폐 단위의 동전이 항상 작은 화폐 단위의 동전의 배수이므로 정당한 알고리즘이다.

:arrow_right: O(K) (K: 화폐 단위의 개수)

2. Knapsack (배낭 채우기)
