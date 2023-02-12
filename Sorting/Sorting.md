# 정렬 알고리즘

데이터를 특정한 기준에 따라 순서대로 나열하는 것

## 선택 정렬 (Selection Sort)

처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 알고리즘

- 처리되지 않은 데이터 중 가장 작은 a을 선택해 가장 앞의 b와 바꾸는 것을 반복하기 때문에, 매번 범위가 줄어드는 선형 탐색을 수행한다.

    ```
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(len(array)):
      min_index = i   # 가장 작은 원소의 인덱스
      for j in range(i + 1, len(array))
        if array[min_index] > array[j]: min_index = j
      array[i], array[min_index] = array[min_index], array[i]         # swap
    print(array)
    ```

- O(N^2) : 전체 연산 횟수 = N + (N-1) + (N-2) +... + 2 = (N^2 + N - 2) / 2


## 삽입 정렬 (Insertion Sort)

처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 알고리즘

- 선택 정렬에 비해 구현 난이도는 높지만, 더 효율적으로 동작한다.

  ```
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1, len(array)):
      for j in range(i, 0, -1):   # 인덱스 i부터 1까지 1씩 감소하며 반복  # stack
        if array[j] < array[j - 1]:   # 한 칸씩 왼쪽으로 이동
          array[j], array[j - 1] = array[j - 1], array[j]
        else: break
    print(array)
  ```
  
- O(N^2)이나 현재 리스트의 **데이터가 거의 정렬되어 있는 상태**라면 매우 빠르게 동작한다. 최선의 경우에는 **O(N)**의 시간복잡도를 가진다.


## 퀵 정렬 (Quick Sort)

기준 데이터를 설정하고 그 기준(Pivot)보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘

- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘으로, 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.

- 가장 기본적인 퀵 정렬의 Pivot은 가장 첫 번째 데이터로 설정된다.

  1. 현재 피벗 값을 설정하고, 왼쪽에서부터는 피벗 값보다 큰 데이터(a)를, 오른쪽에서부터는 피벗 값보다 작은 데이터(b)를 선택하여 a, b를 swap한다.
  2. 만약 a, b의 위치가 엇갈리는 경우에는 b와 피벗의 위치를 서로 변경한다.  
  3. 그럼 b의 위치로 온 피벗을 기준으로 왼쪽과 오른쪽이 각각 피벗보다 작은 값, 큰 값으로 분할(Divide)된다.
        
          Divide: Pivot을 기준으로 데이터 묶음을 나누는 작업
  4. 왼쪽에 있는 데이터 묶음과 오른쪽에 있는 데이터 묶음에 대해서도 동일한 과정을 재귀적으로 정렬 수행한다.

    ```
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    
    def quick_sort(array, start, end):
      if start >= end: return       # 원소가 1개인 경우
      pivot = start
      left = start + 1
      right = end
      while(left <= right):
        # 왼쪽으로부터 피벗보다 큰 값, 오른쪽에서부터 피벗보다 작은 값을 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]): left += 1
        while(right > start and array[right] >= pivot[pivot]): right -= 1
        if left > right: array[right], array[pivot] = array[pivot], array[right]        # 엇갈린 경우
        else: array[left], array[right] = array[right], array[left]
      quick_sort(array, start, right - 1)
      quick_sort(array, right + 1, end)
      
    quick_sort(array, 0, len(array) - 1)
    print(array)
    ```
    
    > 파이썬의 장점을 살린 다른 방식
    ```
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    
    def quick_sort(array):
      if len(array) <= 1: return array
      pivot = array[0]      # 피벗 선택
      tail = array[1:]      # 피벗을 제외한 리스트
      
      left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분(pivot보다 작은 값 묶음)
      right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분(pivot보다 큰 값 묶음)
      
      return quick_sort(left_side) + [pivot] + quick_sort(right_side)
      
    print(quick_sort(array))
    ```

- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(N logN)을 기대할 수 있다.

      너비 * 높이 = N * log N = N log N

- 평균의 경우 O(N log N)의 시간 복잡도를, **최악의 경우(첫 번째 원소를 Pivot으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬) O(N^2)의 시간 복잡도를 가진다.**



## 계수 정렬 (Count Sort)

특정한 조건 (**데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때**)이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘

- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 **시간 복잡도와 공간 복잡도 모두 O(N + K)를 보장**함

    1. 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 리스트 생성
    2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킴
    3. 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 반복하여 인덱스를 출력

    ```
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
      count[array[i]] += 1                              # N 연
    
    for i in range(len(count)):
      for j in range(count[i]): print(i, end=' ')       # N + K 연산
    ```
    
- 때에 따라서 비효율성을 초래할 수 있다.
    
      EX. 데이터가 0과 999,999로 단 2개만 존재하는 경우
- **동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적**으로 사용할 수 있다.


![image](https://user-images.githubusercontent.com/64342804/218288826-888dfedd-6214-40d4-87f0-1fde97ed75b3.png)


## Ex : 두 배열의 원소 교체

두 개의 배열 A, B를 가지고 있을 때 최대 K번의 바꿔치기를 통해 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 구하여라.

- 1 <= N <= 100,000, 0 <= K <= N
- 시간 제한 2초, 메모리 제한 128MB

- 매번 배열 A에서 가장 작은 원소를 골라, 배열 B에서 가장 큰 원소와 교체
- N이 최대 십만 개이므로 최악의 경우 O(N log N)의 알고리즘을 보장하는 정렬 알고리즘을 이용해야 함

```
n, k = map(int, input().split())
a = list(map(int, input().split())
b = list.map(int, input().split())

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]: a[i], b[i] = b[i], a[i]
  else: break

print(sum(a))
```
