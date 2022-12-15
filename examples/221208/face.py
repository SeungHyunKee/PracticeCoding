import cv2
import numpy as np

# https://github.com/opencv/opencv/tree/master/data/haarcascades 다른cascade

# creating face_cascade and eye_cascade objects
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

# 얼굴이미지 가져오기
img = cv2.imread('C://Users//user//Desktop//PracticeCoding//examples//221208//face.png')
print(img)

# print(img.shape)
# cv2.imshow('image show', img)
# cv2.waitKey(0)

# Converting the image into grayscale
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 4 = 박스4개나오게 하는것


# Defining and drawing the rectangles around the face
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2) 
    # 좌표에대한 데이터, (255, 0, 255) 색상, 2 선의굵기
# cv2.imshow('face', img)
# cv2.waitKey(0)

# 관심영역 만들기
roi_gray = gray[y:(y+h), x:(x+w)]
roi_color = img[y:(y+h), x:(x+w)]

# cv2.imshow('face', img)
# cv2.waitKey(0)

# eyes
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)  # 바운딩박스안에있는 얼굴에만 gray_scale 줌
print(eyes)
index = 0

# creating for loop in ordder to divide one eye from another
for(ex, ey, ew, eh) in eyes:
    if index == 0 :
        eye_1 = (ex, ey, ew, eh)
    elif index ==1:
        eye_2 = (ex, ey, ew, eh)
    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
    index = index + 1

if eye_1[0] < eye_2[0] :
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1


# central points of the rectangles

# 왼쪽 눈
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), 
                    int(left_eye[1] + left_eye[3] / 2))
print(left_eye_center)
# 각각의 x, y 가져오기
left_eye_center_x = left_eye_center[0]
left_eye_center_y = left_eye_center[1]

# 오른쪽 눈
right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), 
                    int(right_eye[1] + right_eye[3] / 2))
print(right_eye_center)
# 각각의 x, y 가져오기
left_eye_center_x = left_eye_center[0]
left_eye_center_y = left_eye_center[1]

cv2.circle(roi_color, (left_eye_center), 5, (255, 0, 0), -1)  # -1 : 채우지 않겠다
cv2.circle(roi_color, (left_eye_center), 5, (255, 0, 0), -1) 
# cv2.imshow('face', img)
# cv2.waitKey(0)