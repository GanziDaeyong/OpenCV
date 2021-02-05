"""
gui로 만들기
가상환경에 pip install Pillow
"""
import cv2
import numpy as np
from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageTk

# 경로 및 이름 설정
face_path = r'C:\Users\iwin1\Envs\opencv_practice\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_path = r'C:\Users\iwin1\Envs\opencv_practice\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'
file_name = "./opencv_dnn_202005/image/marathon_01.jpg"
title_name = 'Haar cascade object detection'
frame_width = 500 # 사이즈별로 인식 달라질 수 있다. -> 이걸 바꾸는 실습이다.
image_path = './opencv_dnn_202005/image/marathon_01.jpg'

def selectFile():
    dir = "./opencv_dnn_202005/image" # 편하게 하려고 상대경로 설정
    file_name = filedialog.askopenfilename(initialdir = dir, title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # 루트, 제목, 타입. 여기서는 jpg와 all files 열어줘야 오류 안나더라.
    splitted=file_name.split("/") # 절대경로 넣으면 가끔 인식 못해서 상대경로로 변환
    file_name=dir+"/"+splitted[-1] # 상대경로로 변환
    print('File name : ', file_name)
    # 사진 읽기
    read_image = cv2.imread(file_name) 
    # 사진 기본설정
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    # 사진 tk에 쏴주기 위한 조정
    read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imagetk = ImageTk.PhotoImage(image=image)
    # 기본설정 후 바로 detect함수 호출.
    detectAndDisplay(read_image)


# cascade가 제대로 로드되었는지 확인하는 메서드
def loadCascade(face_path, eyes_path):
    face_cascade= cv2.CascadeClassifier() # 케스케이드 만들어주기
    eyes_cascade= cv2.CascadeClassifier()
    if not face_cascade.load(cv2.samples.findFile(face_path)) or not eyes_cascade.load(cv2.samples.findFile(eyes_path)):
        print('error while loading the cascade')
        return
    print('All path are valid.')
    return face_cascade, eyes_cascade

# 사진에서 얼굴과 눈 찾는 메서드
def detectAndDisplay(frame):
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
    #cv2.imshow('Face detection', frame) # 얘는 윈도우가 바로 새로 뜬다.
    
    # 이미지를 가공해서 보여주는 부분. == tk에 쏴주는 부분.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 그림을 보여주기 위해선 RGB를 컨버트해줘야 한다.
    image = Image.fromarray(image) # 정해진 규격이다. 이것까지는 다루지 않음.
    imagetk = ImageTk.PhotoImage(image=image) # tk inter에 보여주기 위한 과정이다. (강의는 따로.)
    detection.config(image=imagetk)
    detection.image = imagetk
    

# tk inter Main
main = Tk()
main.title(title_name)
main.geometry()

# 사진 불러오기
read_image = cv2.imread(image_path)

# 불러온 사진 조작하기
(height,width) = read_image.shape[:2]
ratio = frame_width/width
dimension = (frame_width, int(height*ratio))
read_image = cv2.resize(read_image, dimension, interpolation=cv2.INTER_AREA) # 디멘션, 설정에 맞게 이미지를 리사이즈한다.
image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB) # 그림을 보여주기 위해선 RGB를 컨버트해줘야 한다.
image = Image.fromarray(image) # 정해진 규격이다. 이것까지는 다루지 않음.
imagetk = ImageTk.PhotoImage(image=image) # tk inter에 보여주기 위한 과정이다. (강의는 따로.)

# cascades 로드하기
(face_cascade, eyes_cascade) = loadCascade(face_path, eyes_path)

# tk inter basic settings
label=Label(main, text=title_name) # 제목
label.config(font=("Courier", 18)) # 폰트
label.grid(row=0,column=0,columnspan=4) # 그리드 형식. 0번째, 0번째칼럼, 4개 칼럼 사이즈로.
sizeLabel=Label(main, text='Frame Width : ')                
sizeLabel.grid(row=1,column=0) # 한 row를 차지.
sizeVal  = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal,from_=0, to=2000, increment=100, justify=RIGHT) 
# main 내에, textvar에는 size를, 0부터 2000 pxl까지, 100만큼 increase, 오른쪽정렬
sizeSpin.grid(row=1, column=1) # 위치를 레이블 옆에.
Button(main,text="File Select", height=2,command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))
# 버튼을 만든다. 클릭하면 lambda로 selectFile()실행. grid는 위치 할당.
detection=Label(main, image=imagetk) # 레이블에서 만든 imagetk 넣음.
detection.grid(row=2,column=0,columnspan=4) # 그 사이즈.
detectAndDisplay(read_image) # 분석하기

main.mainloop()