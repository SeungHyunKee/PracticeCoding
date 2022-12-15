import cv2
import numpy as np
import matplotlib.pyplot as plt


# ex-01
# 이미지_직사각형 직접 그리기
img_rectangle = np.ones((400, 400), dtype='uint8') # ones=1로 다 채워줌
# 위의 코드로 400*400 검은색 사각형 생김
cv2.rectangle(img_rectangle, (50, 50), (300, 300), (255, 255, 255), -1)
# 위의 코드 통해 300*300 흰색((255, 255, 255))으로 채워줌, -1 : 꽉채움
# cv2.imshow("image show", image_rectangle)
# cv2.waitKey(0)

# ex-02
# 원 만들기
img_circle = np.ones((400, 400), dtype='uint8')
cv2.circle(img_circle, (300, 300), 70, (255, 255, 255), -1)
# 검은색 네모안에 흰색 원 생긴것 볼수있음
# cv2.imshow("image show", img_circle)
# cv2.waitKey(0)


# ex-03
# 다양한 크기의 이미지 블렌딩 전, :::비트연산::: 알아보기
''' And연산'''
bitwiseAnd = cv2.bitwise_and(img_rectangle, img_circle)
# cv2.imshow("image bitwiseAnd", bitwiseAnd)
# cv2.waitKey(0)

'''or 연산_____두개다 포함된곳 나옴'''
# bitwiseOr = cv2.bitwise_or(img_rectangle, img_circle)
# cv2.imshow("image bitwiseOr", bitwiseOr)
# cv2.waitKey(0)

'''Xor 연산____교집합부분이 검정색'''
bitwiseXor = cv2.bitwise_xor(img_rectangle, img_circle)
# cv2.imshow("Xor", bitwiseXor)
# cv2.waitKey(0)

'''not 연산'''
rec_not = cv2.bitwise_not(img_rectangle)
# cv2.imshow("rectangle not ", rec_not)
# cv2.waitKey(0)

circle_not = cv2.bitwise_not(img_circle)
# cv2.imshow("circle not ", circle_not)
# cv2.waitKey(0)


# ex-04 마스킹 과제는 흰색대신 이미지를 넣어주시면 됩니다.
#  (원하는 이미지 혹은 얼굴이미지)

# 이미지 읽기
img = cv2.imread('face03.png')

# 마스크 만들기
mask = np.zeros_like(img)
# cv2.rectangle(대상이미지, (원점x, 원점y), 반지름, (색상), 채우기)
cv2.rectangle(mask, (60, 50), (280, 280), (255, 255, 255), -1)
# cv2.rectangle(mask, (420, 50), (550, 230), (255, 255, 255), -1)
# cv2.rectangle(mask, (750, 50), (920, 280), (255, 255, 255), -1)

# 마스킹

masked = cv2.bitwise_and(img, mask)

# 결과출력
imgs = {'original': img, 'mask':mask, 'masked':masked}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]); plt.yticks([])

plt.show()


# cv2.imshow("...", masked)
# cv2.waitKey(0)