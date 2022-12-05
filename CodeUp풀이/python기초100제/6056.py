# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력

a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print((c and not(d)) or (not(c) and d))

# 마지막 출력되는 공식은 그냥 외우기
