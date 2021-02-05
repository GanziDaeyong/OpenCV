import cv2

print("OpenDV version:")
print(cv2.__version__)

img = cv2.imread("dog.png")

print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

# 높이 넓이 픽셀 + 채널 확인 가능하다.

cv2.imshow("dog", img)
cv2.waitKey(0)
cv2.imwrite("cute_dog.jpg", img)
cv2.destroyAllWindows()