import cv2
import numpy as np
from utils import image_show

# 모서리 감지
# 사각형의경우 모서리4개를 찾게되면, 중앙값이나 다른 부가적인값도 유추해낼수있게됨

image_path = "./test01.png"

image_read = cv2.imread(image_path)

image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY) # gray로 받아야함
image_gray = np.float32(image_gray)

block_size = 2  # 모서리 감지 매개 변수 설정
aperture = 29
free_parameter = 0.04 # 이웃하는 픽셀이랑 얼마나 가깝게 할것인지 

detector_response = cv2.cornerHarris(
    image_gray, block_size, aperture, free_parameter)

print(detector_response)

threshold = 0.02
image_read[detector_response > threshold *
           detector_response.max()] = [255, 255, 255]

image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
image_show(image_gray)
