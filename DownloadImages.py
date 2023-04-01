import os
import requests


def checkImageFormat(filename):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        os.remove(filename)
        print(f"{filename} downloaded successfully!")
    else:
        print(f"Could not determine image format for {filename}")


def downloadImage(image_url):
    response = requests.get(image_url)

    if response.status_code == 200:
        content_type = response.headers.get("Content-Type")
        extension = '.' + content_type.split("/")[-1]
        filename = "image" + extension

        with open(filename, "wb") as f:
            f.write(response.content)

        checkImageFormat(filename)
    else:
            print(f"Could not download image, status code: {response.status_code}")


