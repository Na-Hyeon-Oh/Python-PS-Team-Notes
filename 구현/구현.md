# 구현 (Implementation)


- 머릿 속에 있는 알고리즘을 소스코드로 바꾸는 과정

- [ Problem -> Thinking -> Solution ] 

- 흔히 풀이를 떠올리는 것은 쉽지만 소스 코드로 옮기기 어려운 문제를 지칭
    
    - 알고리즘은 간단한데 코드가 긴 문제
    - 실수 연산을 다루고, 특정 소수점 자리까지 출력하는 문제
    - 문자열을 특정한 기준에 따라 끊어 처리하는 문제
    - 적절한 라이브러리를 찾아 사용하는 문제
    
    
## 시뮬레이션

### EX

1. 상하좌우

    여행자가 N * N  크기의 정사각형 공간 위에 서 있고, 해당 공간의 가장 왼쪽 상단 좌표는 (1,1), 가장 오른쪽 하단 좌표는 (N, N)이다.
계획서에는 L(왼쪽으로 한 칸 이동), R, U(위로 한 칸 이동), D 중 하나의 문자가 반복적으로 적혀 있다.
해당 공간에서의 움직임을 벗어나는 여행자의 움직임은 무시된다고 할 때, 최종적인 여행자의 위치를 구하는 문제

```
# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
dist = list(map(str, input().split()))

coor = [1, 1]
for d in dist:
  if d == 'R':
    if coor[1] < n: coor[1] += dy[0]
  elif d == 'L':
    if coor[1] > 1: coor[1] += dy[1]
  elif d == 'D':
    if coor[0] < n: coor[0] += dx[2]
  elif d == 'U':
    if coor[0] > 1: coor[0] += dx[3]

print(f'{coor[0]} {coor[1]}')
```


##  완전 탐색 문제 (Brute Forcing)

### EX

2. 시각

      정수 N이 입력되었을 때 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
      
 ```
 n = int(input())

result = 0

for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k): result+=1

print(result)
 
 ```
 
 ```
 24 * 60 * 60 의 최대 경우의 가짓수도 그리 큰 수가 아님을 
 ```

