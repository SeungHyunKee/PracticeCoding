import numpy as np
import cv2
import matplotlib.pyplot as plt 

# loading an innput image and performing thresholding
img = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)
print(img)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)  

# kernel shape

        # 커널에 따라 마스크의 이진화된 이미지가 어떻게 바뀌는지

# 커널을 담을 빈 리스트 만들기
kernel = []

# 사각형 모형
for i in [cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]:
    kernel.append(cv2.getStructuringElement(i, (11, 11)))

title = ['Rectangle', 'Cross', 'Ellipse']
kernel = np.ones((3,3), np.uint)
plt.figure(figsize=(15, 15))
plt.subplot(2,2,1)
plt.imshow(mask, 'gray')
plt.title('origin')

for i in range(3):
    # erode = 침식
    erosion = cv2.erode(mask, kernel[i])
    plt.subplot(2,2,i+2)
    plt.imshow(erosion, 'gray')
    plt.title(title[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
    



