import os
from deepface import  DeepFace
import cv2


def detecet_face(image_path):

    image = cv2.imread(image_path)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 1.1, 4)
    face_images = []

    index = 0
    for (x, y, w, h) in faces:
        face = image[y: y + h, x: x + w]
        nameOfImage = "face" + str(index) + ".jpg"
        folder_path = "uploadedImages/faces"
        image_path = os.path.join(folder_path, nameOfImage)
        face_images.append(image_path)
        cv2.imwrite(image_path, face)
        index = index + 1


def detect_gender(image_path):

    gender_predictions = []

    detecet_face(image_path)
    folder_path = "uploadedImages/faces"

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):

            image_path = os.path.join(folder_path,filename)
            image = cv2.imread(image_path)
            gender_prediction = DeepFace.analyze(image, actions=['gender'], enforce_detection=False)
            gender_prediction = gender_prediction[0]
            gender_prediction = gender_prediction["dominant_gender"]
            gender_predictions.append(gender_prediction)

    return gender_predictions





