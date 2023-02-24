from GenderDetectionModel import detect_gender
import cv2


if __name__ == '__main__':

    Image_path = input("Enter the image path: ")

    Image = cv2.imread(Image_path)

    detect_gender(Image)

