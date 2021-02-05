import cv2

print("OpenDV version:")
print(cv2.__version__)

img = cv2.imread("dog.png")

print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

# 높이 넓이 픽셀 + 채널 확인 가능하다.
#cv2.imshow("dog", img)

(b, g, r) = img[0,0] 

# bgr 순은 관습이다.
print("Pixel at(0, 0) - Red: {}, Green: {}, Blue: {}". format(r,g,b))

dot = img[50:100, 50:100]
# cv2.imshow("dot", dot)
img[50:100, 50:100] = (0,0,255)
# #가로50~100, 세로50~100.
#cv2.imshow("red", img)

cv2.rectangle(img, (150,50), (200,100), (0,255,0),5)
cv2.circle(img, (275,75), 25, (0,255,255),-1)
cv2.line(img, (350,100), (400,100), (255,0,0), 5)
cv2.putText(img, 'Daeyong', (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 4)
# cv2.rectangle : 이미지, 가로, 세로, 색, 선두께
# cv2.circle : 이미지, 중심, 반지름, 색, 선두께 (-1: 전체를 다 채운다.)
# cv2.line : 이미지, 시작좌표, 끝좌표, 색, 선두께
# cv2.putText : 이미지, 텍스트, 시작위치, 폰트 종류, 폰트크기, 색, 선두께
cv2.imshow("draw", img)
cv2.waitKey(0)
cv2.destroyAllWindows()