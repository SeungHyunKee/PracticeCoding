# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력

a, b = map(int, input().split())

print(bool(a) and bool(b))

# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 나머지 경우는 False 로 계산
