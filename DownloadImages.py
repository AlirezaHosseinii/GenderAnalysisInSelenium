import os
import requests
import imghdr


def checkImageFormat(filename):
    if imghdr.what(filename) is None:
        os.remove(filename)
        print(f"Could not determine image format for {filename}")
    else:
        print(f"{filename} downloaded successfully!")


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


