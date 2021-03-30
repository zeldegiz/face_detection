#import library
import cv2

#face detection function
def face_detect(img_path):
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#Read Cascade Classifier
  gray_img = cv2.imread(img_path,0)#Read grayscale image 
  faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)#Detect faces in image
  return faces
  
#example
img_path = "img.jpg"
faces = face_detect(img_path)
