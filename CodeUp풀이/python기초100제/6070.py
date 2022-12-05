# 6070 

'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
'''

# if 조건 or 조건 or 조건

# if n == 1 or 2 or 12: (x)  -->  2, 12 가 무조건 true가 됨

# if n == 1 or n == 2 or n == 12: (o)


n = int(input())
if n == 1 or n == 2 or n == 12:
    print('winter')
elif n == 3 or n==4 or n==5:
    print('spring')
elif n == 6 or n==7 or n==8:
    print('summer')
else:
    print('fall')



# n = int(input())
# if n in [12,1,2]:   # 이렇게 리스트로도 표현할수있다
#     print('winter')
# elif n == 3 or n==4 or n==5:
#     print('spring')
# elif n == 6 or n==7 or n==8:
#     print('summer')
# else:
#     print('fall')    




# 틀린방법
# n = int(input())
# if n == 1 or 2 or 12:
#     print('winter')
# elif n == 3 or 4 or 5:
#     print('spring')
# elif n == 6 or 7 or 8:
#     print('summer')
# else:
#     print('fall')    