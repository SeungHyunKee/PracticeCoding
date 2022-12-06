''' 이미지를 머신러닝에 필요한 샘플로 변환하려면 넘파이의 flatten()사용
Flatten() : 이미지데이터가 담긴 다차원배열 -> 샘플값이 담긴 벡터로 변환'''

import cv2
from utils import image_show

image_path = "./cat.jpg"
# 그레이 이미지 변경
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

image_10x10 = cv2.resize(image_gray, (10, 10))
image_10x10.flatten()  # 이미지 데이터를 1차원 백터로 변환
image_show(image_10x10)
