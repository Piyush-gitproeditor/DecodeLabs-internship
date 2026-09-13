import cv2
import pytesseract

# Image Loading 
image =cv2.imread("input/image.jpg")

#Checking for the image 
if image is None:
    print("Error- Image not found !")
    exit()

# Extracting text
text = pytesseract.image_to_string(image)

# End results
print("\n        Recognized text       \n")
print(text)
print("\n                               \n")