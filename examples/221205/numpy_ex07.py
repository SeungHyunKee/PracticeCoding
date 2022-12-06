import numpy as np

# 7. 넘파이배열 객체 복사

# # COPY 버전
# array1 = np.arange(0, 10)
# array2 = array1.copy() # copy를 하면 아예 새로운 주소에 넣게됨
# array2[0] = 99
# print(array1)
# print(array2)

# # [0 1 2 3 4 5 6 7 8 9] >> array1
# # [99  1  2  3  4  5  6  7  8  9] >> array2



# # numpy 중복된 원소 제거
# array = np.array([1, 2, 1, 2, 3, 4, 3, 4, 5])
# print("중복 처리 전 >> ", array)
# # 중복 처리 전 >>  [1 2 1 2 3 4 3 4 5]
# print("중복 처리 후 >> ", np.unique(array))

# # 중복 처리 전 >>  [1 2 1 2 3 4 3 4 5]
# # 중복 처리 후 >>  [1 2 3 4 5]



# np.isin() : 내가 찾는게 있는지 여부 - 각 index 위치에 true false
array = np.array([1, 2, 3, 4, 5, 6, 7])

iwantit = np.array([1, 2, 3, 10]) # 내가 찾는값

print(np.isin(array, iwantit))
# [ True  True  True False False False False]
