'''
0이 아닌 정수 1개가 입력되었을 때, 
음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력
'''

n = int(input())

if n < 0 and n % 2 == 0:
    print('A')
elif n < 0 and n % 2 == 1:
    print('B')
elif n > 0 and n % 2 == 0:
    print('C')
else:   
    print('D')    

