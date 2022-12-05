# 주성분을 사용해 특성줄이기
# 사이킷런 손글씨데이터 활용해 특성행렬을 표준화처리및 주성분특성 줄이기

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from skleran import datasets
# pip install sklearn

digits = datasets.load_digits()
print(digits)