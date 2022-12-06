import sklearn
from sklearn.preprocessing import*
import numpy as np
from numpy import*

# pip install sklearn
def normalization(data):
    data_mm = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    return data_mm

def numpy_standardization(data):
    '''
    (각 데이터 - 평균(각 열)) / 표준편차(각 열)
    '''
    std_data= (data - np.mean(data, axis = 0) / np.std(data, axis=0))
    return std_data 
    # mean() : 평균구해주는 함수, xis = 0


def main():
    data = np.random.randint(30, size = (6,5))
    print(data)
    std_data_temp = np.standardization(data)
    print(std_data_temp)

if __name__ == '__main__':
    main()
    # 5*5 랜덤값 만든다

