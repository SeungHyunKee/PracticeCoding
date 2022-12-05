# 이미지 사이즈변경

# 한번에 이미지 바뀐거 보기 위해 matplotlib 사용
import cv2

import matplotlib.pyplot as plt

image_path = "./cat.jpg"

# 이미지 읽기
image = cv2.imread(image_path)
# RGB 타입 변환
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 사이즈 변환
image_50x50 = cv2.resize(image_rgb, (50, 50))


flg, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image_rgb)
ax[0].set_title("Original Image")
ax[1].imshow(image_50x50)
ax[1].set_title("Resize Image")
plt.show()



# # 이미지 저장 : imwrite(저장경로) 저장하고자하는 이미지

# cv2.imwritet('./cat_image_50x50.png', image_50x50)
# # png로 저장하는게 용량은 더 크지만, 고화질이다
