import os

from deepface import  DeepFace
import cv2

def detect_gender(image):


    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) , 1.1, 4)


    index = 0
    for (x, y, w, h) in faces:
        face = image[y: y + h, x: x + w]
        nameOfImage = "face" + str(index) + ".jpg"

        cv2.imwrite(nameOfImage , face)

        image_to_predict = cv2.imread(nameOfImage)

        gender_prediction = DeepFace.analyze(image_to_predict, actions=['gender'], enforce_detection=False)
        gender_prediction = gender_prediction[0]
        gender_prediction = gender_prediction["dominant_gender"]
        print(nameOfImage + " is " + gender_prediction)

        index = index + 1






