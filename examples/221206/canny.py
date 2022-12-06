# 경계선 감지
# canny() 메소드 활용해 경계선 감지할수있다

import numpy as np
import cv2
from utils import image_show

# 이미지 읽기
image = cv2.imread('./test.jpg')

# 경계선 찾기 : canny() 할때는 무조건 gray scale로 바꿔줘야함
image_gray = cv2.imread('./test.jpg', cv2.IMREAD_GRAYSCALE)
# 중간값 찾기
mdeian_intensity = np.median(image_gray)

# 중간 픽셀 강도에서 위아래 1표준편차 떨어진 값을 임계값으로 설정
lower_threshold = int(max(0, (1.0 - 0.33) * mdeian_intensity))
upper_threshold = int(min(255,  (1.0 + 0.33) * mdeian_intensity))

# Canny edge Detection 적용
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)
image_show(image_canny)
