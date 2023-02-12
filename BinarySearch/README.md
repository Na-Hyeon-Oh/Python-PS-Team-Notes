# 이진 탐색 알고리즘

정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

      * 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법

- 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2 N에 비례한다.
- 즉, 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(log N)을 보장한다.

Ex. 재귀적 구현

  ```
  def binary_search(array, target, start, end):
    if start > end: return None
    mid = (start + end) // 2
    
    if array[mid] == target: return mid
    elif array[mid] > target: return binary_search(array, target, start, mid - 1)
    else: return binary_search(array, target, mid + 1, end)
  
  n, target = list(map(int, input().split()))
  array = list(map, int, input().split()))
  
  result = binary_search(array, target, 0, n - 1)
  if result == None: print("원소가 존재하지 않습니다.")
  else: print(result + 1)
  ```

Ex. 반복문 구현

  ```
  def binary_search(array, target, start, end):
    while start <= end:
      mid = (start + end) // 2
      
      if array[mid] == target: return mid
      elif array[mid] > target: end = mid -1
      else: start = mid + 1
    return None
  
  n, target = list(map(int, input().split()))
  array = list(map, int, input().split()))
  
  result = binary_search(array, target, 0, n - 1)
  if result == None: print("원소가 존재하지 않습니다.")
  else: print(result + 1)
  ```
  

## 파이썬 이진 탐색 라이브러리

- bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
- bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

    ```
    from bisect import bisect_left, bisect_right
    
    a = [1, 2, 4, 4, 8]
    x = 4
    print(bisect_left(a, x))      # 2
    print(bisect_right(a, x))       # 4
    ```
    
    
 ### 응용: 값이 특정 범위에 속하는 데이터 개수 구하기
 
 ```
 from bisect import bisect_left, bisect_right
 
 # 값이 [left_value, right_value]인 데이터의 개수를 반환
 def count_by_range(a, left_value, right_value):
  right_idx = bisect_right(a, right_value)
  left_idx = bisect_left(a, left_value)
  return right_idx - left_idx
 
 a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
 print(count_by_range(a, 4, 4))   #2  
 print(count_by_range(a, -1, 3))  #6
 ```
 
 
 ## Parametric Search
 
 최적화 문제를 결정 문제(yes / no)로 바꾸어 해결하는 기법
 
 Ex. 특정한 조건을 만족하는 가장 알맞은 값을 가장 빠르게 찾는 최적화 문제
 
 - 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.

### EX

1. 떡볶이 떡 만들기

      - 절단기에 높이(H; 0 <= H < 1,000,000,000)를 지정하면 줄지어진 떡을 한 번에 절단한다고 했을 때, 높이가 H보다 긴 떡만 잘리게 된다. 잘린 남은 떡을 손님이 가져간다.
      - 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
      - 떡의 개수 N, 떡의 길이 M (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
      - 시간 제한 1초, 메모리 제한 128MB


            - 절단기의 높이가 10억까지의 정수로 매우 큰 탐색 범위이므로 이진 탐색을 떠올리기 
            - 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하기

            ```
            n, m = list(map(int, input().split(' ')))
            array = list(map(int, input().split()))
            
            start = 0
            end = max(array)
            
            result = 0
            # 이진 탐
            while(start <= end):
              total = 0
              mid = (start + end) // 2
              for x in array:
                if x > mid: total += x - mid
              if total < m: end = mid - 1     # 떡이 부족한 경우 (왼쪽 부분 탐색)
              else:
                result = mid      # 지금까지의 탐색 중 가장 최적화된 결과
                start = mid + 1
                
             print(result)
            ```

2. 정렬된 배열에서 특정 수의 개수 구하기

    - N개의 원소를 포함하고 있는 수열이 오름차순으로 **정렬**되어 있을 때 수열에서 x가 등장하는 횟수 계산하기
    - x가 없다면 -1 출력
    - **log N을 보장하는 알고리즘을 설계하지 않으면 시간 초과**
    - 1 <= N <= 1,000,000, -10^9 <= x <= 10^9
    - 시간 제한 1초, 메모리 제한 128MB

          - 선형 탐색으로는 시간 초과 판정 받
          - 데이터 정렬 -> 이진 탐색 수행 가능
          - 특정 값이 등장하는 첫번째 위치와 마지막 위치를 찾아 그 차이를 계산하여 문제 해결 가능 

           ```
           from bisect import bisect_left, bisect_right
           
           def count_by_range(array, left_value, right_value):
            right_idx = bisect_right(array, right_value)
            left_idx = bisect_left(array, left_value)
            return right_idx - left_idx
            
           n, x = map(int, input().split())
           array = list(map(int, input().split()))
           
           count = count_by_range(array, x, x)
           if count == 0: print(-1)
           else: print(count)
           ```
