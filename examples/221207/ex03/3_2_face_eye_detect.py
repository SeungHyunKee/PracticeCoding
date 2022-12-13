import cv2
import numpy as np

# python에서 OpenCV로 얼굴정렬

'''
1. 얼굴 및 눈 감지 위해 OpenCV Hear 캐스케이드 구성(정면얼굴 감지및 눈 감지 모듈)을 사용
 face_casacade, eye_casacade 이 두 객체에 감지된 얼굴과 눈을 저장

2.1 얼굴이미지 데이터 읽기
2.2 얼굴이미지 바운딩 박스 : 케스케이드 경우 그레이스케일 이미지에서만 작동

3. 눈 감지 : 사각형안에 위치할 두개의 관심영역 만들기
 1) 눈 감지할 회색조 이미지 영역, 2) 사각형 그릴 컬러이미지 필요

4. left_eye , right_ eye

5. 두 눈의 중심점 사이에 선 긋기, 그전에 직사각형 중심점 좌표 계산하기

6. 수평선 그리고 그 선과 눈의 두 중심점을 연결하는 
   선 사이의 각도 계산 : 최종목적=이 각도를 기준으로 이미지 회전시키는것

7. 왼쪽눈 y 좌표가 오른쪽는 y좌표보다 크면 이미지를 시계방향으로 회전한다. 반대는 반시계방향

8. 이미지를 각도 \theta 만큼 회전할수있음

9. 이미지 크기 조정 : 눈 사이의 거리를 참조프레임으로 사용
'''


# 1. 얼굴 및 눈 감지 위해 OpenCV Hear 캐스케이드 구성(정면얼굴 감지및 눈 감지 모듈)을 사용
#  >>> face_casacade, eye_casacade 이 두 객체에 감지된 얼굴과 눈을 저장
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 2.1 얼굴이미지 데이터 읽기 _ loading the image
face_img = cv2.imread('face.png')
face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(face_gray, 1.1, 4)

# 2.2 얼굴이미지 바운딩 박스 >>> 케스케이드의 경우 그레이스케일 이미지에서만 작동
for(x,y,w,h) in faces:
    cv2.rectangle(face_img, (x,y), (x+w, y+h), (0,255,0), 3)

    roi_img = face_img[y:y+h, x:x+w]  # 원본 남겨놓음
    roi_gray = face_gray[y:y+h, x:x+w] #
    cv2.imshow('roi', roi_img)
    cv2.waitKey(0)

# 3. 눈 감지 : 사각형안에 위치할 두개의 관심영역 만들기
# roi = 관심영역
# face 전체에서 관심영역만 빼옴

eyes = eye_casacade.detectMultiScale(roi_gray, 1.1, 4)
print(eyes)

for(x,y,w,h) in eyes:
    cv2.rectangle(roi_image, (x,y), (x+w, y+h), (0,255,0), 3)

    roi_img = face_img[y:y+h, x:x+w] #이뒤에 .copy[] 해주지 않으면 원본이미지에 영향을 끼침
    roi_gray = face_gray[y:y+h, x:x+w] 

# cv2.imshow('face box', face_img)
# cv2.waitKey(0)
