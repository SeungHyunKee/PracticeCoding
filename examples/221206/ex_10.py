import cv2
from utils import image_show
import numpy as np

# 머신러닝 특성만들기
# 컬러이미지 10* 10 / 컬러이미지 255*255

image_path = "./cat.jpg"
image = cv2.imread(image_path)
# image 10x10 픽셀 크기로 변환
image_color_10x10 = cv2.resize(image, (10, 10))
image_color_10x10.flatten()
# image_show(image_color_10x10)

# image 225x255 픽셀 크기로 변환
image_color_225x255 = cv2.resize(image, (225, 255))
image_color_225x255.flatten()
image_show(image_color_225x255)

# x = np.array([[51, 40], [14, 19], [10, 7]])
# x = x.flatten()
# print(x)
# '''결과 [51 40 14 19 10 7]
# '''