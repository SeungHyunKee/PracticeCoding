# 가우시안 필터 적용
# 가우시안 필터의 함수는 이벤트가 평균값을 중심으로 발생할 확률을 나타냄
import cv2
import numpy as np
from utils import image_show

img = cv2.imread('./car.jpg', 0)
print(img.shape)
img_rsize = cv2.resize(img, (320, 240))  # 이미지 사이즈조절

Gaussian_blurred_1 = np.hstack([  # hstack() :배열 옆으로
    cv2.GaussianBlur(img_rsize, (3, 3), 0),  # 왼쪽 : 3*3필터
    cv2.GaussianBlur(img_rsize, (5, 5), 0),  # 가운데 : 5*5필터
    cv2.GaussianBlur(img_rsize, (9, 9), 0),  # 오른쪽 : 9*9필터
])
image_show(Gaussian_blurred_1)
cv2.imwrite("gaussian_blur.png", Gaussian_blurred_1)