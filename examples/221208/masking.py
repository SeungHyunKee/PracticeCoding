import cv2
import numpy as np


mask = np.zeros((683, 1024), dtype='uint8')
cv2.rectangle(mask, (60, 50), (280, 280), (255, 255, 255), -1)
cv2.rectangle(mask, (420, 50), (550, 230), (255, 255, 255), -1)
cv2.rectangle(mask, (750, 50), (920, 280), (255, 255, 255), -1)






cv2.imshow("...", mask)
cv2.waitKey(0)