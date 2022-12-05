import numpy as np

# 4. Numpy원소의 정렬 - 각 열을 기준으로 정렬

array = np.array([[5, 2, 7, 6], [2, 3, 10, 15]])
print("각 열을 기준으로 정렬 전 \n", array)
# 각 열을 기준으로 정렬 전 
#  [[ 5  2  7  6]
#  [ 2  3 10 15]]


# 열기준정렬 : .sort(axis=0), 행기준정렬 : .sort(axis=1)
array.sort(axis=0) 
print("각 열을 기준으로 정렬 후 \n", array)
# 각 열을 기준으로 정렬 후 
#  [[ 2  2  7  6]
#  [ 5  3 10 15]]
