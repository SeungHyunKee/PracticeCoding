# 같은 크기의 이미지 블렌딩 실험
# 이미지 블렌딩 및 붙여넣기 

import numpy as np
import cv2
import matplotlib.pyplot as plt

large_img = cv2.imread('./ex_image.png')
watermakr = cv2.imread('./ex_image_logo.png')

print ('large_image size >>> ', large_img.shape)
print ('watermakr image size >>> ', watermakr.shape)

# cv2.imshow('image large', large_img)
# cv2.imshow('watermakr', watermakr)
# cv2.waitKey(0)
# 결과 : 두개의 이미지가 크기가 다름(로고사진이 더 작음)
# -> 두 사진의 크기 맞춰주기 : resize()

img1 = cv2.resize(large_img,(800,600))
img2 = cv2.resize(watermakr,(800,600))
# cv2.imshow('image large', img1)
# cv2.imshow('watermakr', img2)
# cv2.waitKey(0)
# -> 두사진이 크기 같아진걸 확인할수있음
print('img resize >>', img1.shape)
print('watermakr >>', img2.shape)
''' --------- 수치로 확인해보기 --------------
large_image size >>>  (683, 1024, 3)
watermakr image size >>>  (593, 795, 3)
img resize >> (600, 800, 3)
watermakr >> (600, 800, 3)----------------'''


## 혼합 진행 ##

# 처음 0.5 값 설정 _ 베이스 5:5
# blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  # 0.5 =반정도 투명하게 설정, 0.9 = 더 선명,  0 = 감마포인트
# cv2.imshow('image show', blended)
# cv2.waitKey(0)

# 9:1
# 결과 : 로고가 굉장히 흐리고, 사람이미지 거의 뚜렷하게 출력됨
# blended = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
# cv2.imshow('image show', blended)
# cv2.waitKey(0)


# 1로 설정 
# 결과 : 모든값이 흰색으로 출력되므로 뒤에있는 사람이미지img1이 전부 흰색으로 출력됨
# blended = cv2.addWeighted(img1, 1, img2, 1, 0)
# cv2.imshow('image show', blended)
# cv2.waitKey(0)

# # 높은 값으로 전달 
# # blended = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)

# # 1로 설정 
# blended = cv2.addWeighted(img1, 1, img2, 1, 0)
# cv2.imshow("img show", blended)
# cv2.waitKey(0)