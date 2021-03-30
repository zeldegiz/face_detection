#import library
import cv2 #opencv version is 4.5.1
from mtcnn_cv2 import MTCNN #install with -- pip install mtcnn-opencv

#face detection function
def face_detect(img_path):
  detector = MTCNN()
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  faces = detector.detect_faces(img)
  return faces

#example
img_path = "img.jpg"
faces = face_detect(img_path)
