import numpy as np

# 2. 복수 객체 저장을 위한 데이터 생성
# 복수개의 array(배열) 만들기
array1 = np.arange(0, 10) # [0 1 2 3 4 5 6 7 8 9]
array2 = np.arange(0, 20) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(array1, array2)

# 저장하기
np.savez('./save.npz', array1=array1, array2=array2)

# 객체 불러오기
data = np.load('./save.npz')
result1 = data['array1']  # 저장할때 키값인 array1 
result2 = data['array2']

print("result1 >> ", result1)
print("result2 >> ", result2)

# result1 >>  [0 1 2 3 4 5 6 7 8 9]
# result2 >>  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
