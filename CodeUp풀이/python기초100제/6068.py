# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력
'''
평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.
'''

n = int(input())
if 90 <= n <= 100:
    print('A')
elif 70 <= n <= 89:
    print('B')
elif 40 <= n <= 69:
    print('C')
else:
    print('D')