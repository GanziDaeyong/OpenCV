import cv2
import numpy as np

def loadCascade(face_path, eyes_path):
    face_cascade= cv2.CascadeClassifier()
    eyes_cascade= cv2.CascadeClassifier()
    if not face_cascade.load(cv2.samples.findFile(face_path)) or not eyes_cascade.load(cv2.samples.findFile(eyes_path)):
        print('error while loading the cascade')
        return
    print('All path are valid.')
    return face_cascade, eyes_cascade

def detectAndDisplay(frame, face_cascade, eyes_cascade):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gray가 더 정확하다.
    frame_gray - cv2.equalizeHist(frame_gray) # histogram을 통해 단순화한다.
    # 1. 얼굴찾기
    faces = face_cascade.detectMultiScale(frame_gray) # splitted 그림을 특정 영역화한다.
    for (x,y,w,h) in faces: # x축 y축 width height
        center = (x+w//2, y+h//2) # 정확히 중간 지점
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 4) # 그림, 양 대각선 끝 모서리 두 점, 색, 두께
        faceROI = frame_gray[y:y+h, x:x+w] # 금방 선택한 얼굴만 끄집어낸다. 
        # 2. 각 얼굴에서 눈 찾기
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes :
            eye_center = (x+x2+w2//2, y+y2+h2//2) # 눈의 중간지점
            radius = int(round((w2+h2)*0.25)) # 가상의 반지름 값.
            frame = cv2.circle(frame, eye_center, radius, (255,0,0), 4)
        cv2.imshow('Face detection', frame)

path = "opencv_dnn_202005/image/marathon_01.jpg"
img = cv2.imread(path)

cv2.imshow("Original image", img)
(height,width) = img.shape[:2]
cv2.imshow("Original image", img)

face_path = r'C:\Users\iwin1\Envs\opencv_practice\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_path = r'C:\Users\iwin1\Envs\opencv_practice\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'
# cascade는 기본 제공된다. -> 이를 사용하기 때문에 flexible하지 못한 것이다.
# 위치는 단순히 가상환경 라이브러리 설치 위치이다.



# 1. load cascades
(face_cascade, eyes_cascade) = loadCascade(face_path, eyes_path)
detectAndDisplay(img, face_cascade, eyes_cascade)


cv2.waitKey(0)
cv2.destroyAllWindows()