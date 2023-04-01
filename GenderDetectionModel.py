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
        nameOfFaceImage = f"{os.path.basename(image_path)}Face{str(index)}.jpg"
        folder_path = "uploadedImages/faces"
        faceImage_path = os.path.join(folder_path, nameOfFaceImage)
        cv2.imwrite(faceImage_path, face)
        face_images.append(faceImage_path)
        index = index + 1


def checkImageFormat(filename):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        return True
    else:
        print(f"Could not determine image format for {filename}")
        exit(1)


def countNumberOfGenders(prediction):
    N_men = prediction.count("Man")
    N_women = prediction.count("Woman")
    return N_men,N_women


def detect_genders(image_path):
    gender_predictions = []

    detecet_face(image_path)
    folder_path = "uploadedImages/faces"

    for filename in os.listdir(folder_path):
        if(checkImageFormat(filename)):
            image_path = os.path.join(folder_path,filename)
            image = cv2.imread(image_path)
            gender_prediction = DeepFace.analyze(image, actions=['gender'], enforce_detection=False)
            gender_prediction = gender_prediction[0]
            gender_prediction = gender_prediction["dominant_gender"]
            gender_predictions.append(gender_prediction)


    N_men, N_women = countNumberOfGenders(gender_predictions)

    return gender_predictions,N_men,N_women





