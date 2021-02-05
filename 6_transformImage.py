import cv2
import numpy as np
img = cv2.imread("dog.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2] 
center = (width//2, height//2) 
#height에 0을, width에는 1을 준다.
# // -> 몫을 리턴한다.

cv2.imshow("dog", img)
"""
# 이미지 위치옮기기
move = np.float32([[1,0,100], [0,1,-300]]) # 이거 자체가 width, height를 의미한다.
# 0,1 -> 위아래를 의미한다. 양수는 아래로, 음수는 위로.
# 1,0 -> 좌우를 의미한다. 양수는 좌로, 음수는 우로.
moved = cv2.warpAffine(img, move, (width, height))
# float로 아주 정밀하게 움직일 수 있다.
# move와 warpAffine은 cv2 제공 메서드이다. 옮기는 것.
cv2.imshow("Moved down: +, up: - and right : +, left - ", moved)

# 이미지 회전시키기
move = cv2.getRotationMatrix2D(center,-90,0.3) 
# 돌릴 중심점, 돌릴 각도, scale 값 / 돌릴 각도는 -가 시계방향, +가 반시계.
rotated = cv2.warpAffine(img,move,(width, height))
cv2.imshow("Rotated degrees", rotated)
"""
"""
# 이미지 크기 변경하기
ratio = 200.0/width # 200으로 줄일 거니까, 그 ratio를 구해놔야 사진이 정방향으로 줄어든다.
dimension = (200, int(height*ratio)) # width는 200으로, height는 그에 비례하게.
resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA) 
#이미지, 차원, (옵션)보간법(영역보간법) -> INTER_LINER / INTER_CUBIC / INTER_REALIST 등도 있다.
cv2.imshow("resized", resized)
"""

# 이미지 뒤집기
flipped = cv2.flip(img, 1) # horizontal=1, vertical=0, both=-1
cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()