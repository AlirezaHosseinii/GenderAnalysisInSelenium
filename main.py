from GenderDetectionModel import  detect_genders

image_path = input("Enter the image path: ")

if __name__ == '__main__':
    gender_predictions , N_men , N_women  =  detect_genders(image_path)
    print(gender_predictions)
    print(f"the number of men: {N_men}")
    print(f"the number of women: {N_women}")