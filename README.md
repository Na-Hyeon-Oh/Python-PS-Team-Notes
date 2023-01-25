# Python-PS-Team-Notes

## 요구 사항에 따라 적절한 알고리즘 설계하기

### 시간 복잡도

연산횟수를 (N)이라고 할 때, Python에서 설계해야 하는 알고리즘의 시간 복잡도는 다음과 같다. 

> 1초에 20,000,000 번 계산 가능

- N ~= 500 -> O(N^3)
- N ~= 2,000 -> O(N^2)
- N ~= 100,000 -> O(NlogN)
- N ~= 10,000,000 -> O(N)


## Python Library

1. 내장 함수

     기본 입출력 함수, 정렬 함수

      ex. sum([]), 
      
      min(), max(), 
      
      eval(),               
      > 수식으로 표현된 식(ex. (3+5)*7)을 계산한 결과 반환
      
      print(),
      
      sorted([], key=, reverse=)            
      >  정렬 기준 -> key (ex.lambda x:x[1]  # 각 tuple의 두번째 원소 기준 정렬)

2. itertools

    순열, 조합, 중복순열, 중복조합
    
     ex. permutations([], r), 
     
     combinations([], r),
     
     product([], repeat=),
     
     combinations_with_replacement([], r)

3. heapq

    힙 자료 구조 (우선순위 큐)

     ex. heapq.heappush, heapq.heappop
     
     ref. https://www.daleseo.com/python-heapq/ 

4. bisect

    Binary Search

5. collections

    덱(deque), counter 등의 자료구조
    
     ex.
      ```
      from collections import Counter

      counter = Counter(['red', 'blue', 'blue'])
      print(counter['blue'])  # blue 가 등장한 횟수
      ```

6. math

    factorial, 제곱근, 최대공약수(gcd), 삼각함수, 파이(pi) 등의 상수

     ex. 
      ```
      import math
      
      def lcm(a, b):
          return a*b // math.gcd(a,b)
      ```
