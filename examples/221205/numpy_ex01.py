import numpy as np

# 1. 단일 객체 저장 및 불러오기

# 단일객체, 즉 하나의 배열을 만든다
array = np.arange(0, 10) # 배열안에 0~9 채워넣음
print(array)

# 결과 -> [0 1 2 3 4 5 6 7 8 9]

# .npy 파일에다가 저장하기 : np.save() _ 고정된 배열 가지고와서 계산할때 많이 사용
np.save("./save.npy", array)  # 현재위치에 경로지정해서 저장

# 불러오기  : np.load(현재저장된 위치 주소)
result = np.load('./save.npy')
print("result >> ", result)
