# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력

a = int(input())
print(~a)


# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.
# (~ : tilde, 틸드라고 읽는다.)

#  1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면
#         00000000 00000000 00000000 00000001 이고,
# ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

# 예시
# a = 1
# print(~a) #-2가 출력된다.

# 참고
# 컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다.
# 0과 1로만 구성되는 비트단위들로 변환되어 저장되는데,
# 양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 "2의 보수 표현"방법으로 저장된다.