# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램

a, b = map(int, input().split())
c = (a if(a>b) else b)
print(c)

# c는 아래 코드와 동일하다
# if a>b:
#     print(a)
# else:
#     print(b) 