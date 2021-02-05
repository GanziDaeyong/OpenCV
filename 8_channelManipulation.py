import cv2
import numpy as np
img = cv2.imread("dog.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2] 
center = (width//2, height//2) 

cv2.imshow("dog", img)  

(Blue, Green, Red) = cv2.split(img)
"""
# 이미지를 채널별로 split.
cv2.imshow("Red", Red)
cv2.imshow("Green", Green)
cv2.imshow("Blue", Blue)
cv2.waitKey(0)
"""

# 이미지를 특정 색으로 merge
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros,zeros,Red]))
cv2.imshow("Green", cv2.merge([zeros,Green,zeros]))
cv2.imshow("Blue", cv2.merge([Blue,zeros,zeros]))
# merge에서 나머지를 zero로 채우면, 특정 색으로만 완전히 merge함.

"""
# 이미지에 필터 씌우기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayFilter", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSVFilter", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LABFilter", lab)
"""

# 이미지에 색 합치기
BGR = cv2.merge([Blue, Green, Red])
# 다시 bgr을 merge하여 원래 이미지로 롤백한다. 
cv2.imshow("remerged", BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

