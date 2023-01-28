'''정수 1개가 입력된다.
(0 ~ 100)
0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.'''

a = int(input())
b = 0
while b <= a :
    print(int(b), end = '\n')
    b += 1