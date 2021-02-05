import cv2
import numpy as np
img = cv2.imread("dog.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2] 
center = (width//2, height//2) 
print(center)
cv2.imshow("dog", img)  

mask = np.zeros(img.shape[:2], dtype="uint8")
#height와 width 영역을 .zero(까맣게) 채운다.
cv2.circle(mask, center, 100, (255,255,255), -1) # -1은 다 채운다는 의미.
cv2.imshow("Mask", mask)

# Bitwise operation.
masked = cv2.bitwise_and(img, img, mask=mask) # 어차피 논리합이니까 img 중복 상관없다.
cv2.imshow("Masked dog", masked)

# Image blending 한번 살펴보기

cv2.waitKey(0)
cv2.destroyAllWindows()