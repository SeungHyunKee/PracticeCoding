# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용

a, b, c = map(int, input().split())
d = (b if(a>b) else a)
e = (c if(d>c) else d)
print(e)


# if a > b :
#     d = b
# elif d > c:
#     e = 



# 텍스트 데이터 처리 01
import re
text_data = [" Interrobang. By Aishwarya Henriette",
             "Parking and going. By Kear Gua",
             "Today Is the night. By Jar par"]

# 공백 제거
strip_whitespace = [string.strip() for string in text_data]
print("공백 제거 >> ", strip_whitespace)

# 마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print("마침표 제거 >> ", remove_periods)
"""
결과 
공백 제거 >>  ['Interrobang. By Aishwarya Henriette', 'Parking and going. By Kear Gua', 'Today Is the night. By Jar par']
마침표 제거 >>  ['Interrobang By Aishwarya Henriette', 'Parking and going By Kear Gua', 'Today Is the night By Jar par']
"""


def capitalizer(string: str) -> str: return string.upper()
# ['INTERROBANG BY AISHWARYA HENRIETTE', 'PARKING AND GOING BY KEAR GUA', 'TODAY IS THE NIGHT BY JAR PAR']


temp = [capitalizer(string) for string in remove_periods]
print(temp)


def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)


data = [replace_letters_with_X(string) for string in remove_periods]
print(data)
