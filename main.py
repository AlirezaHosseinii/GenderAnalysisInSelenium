from GenderDetectionModel import  detect_gender

image_path = input("Enter the image path: ")

if __name__ == '__main__':
    gender_predictions =  detect_gender(image_path)
    print(gender_predictions)