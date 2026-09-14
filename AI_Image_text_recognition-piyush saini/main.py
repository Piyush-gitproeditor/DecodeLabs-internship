import cv2
import pytesseract

# Load the image
image = cv2.imread("input/image.jpg")

# Check if image was loaded successfully
if image is None:
    print("ERROR: Image could not be loaded.")
    exit()

print("Image loaded successfully!")
print("Image size:", image.shape)

# Perform OCR
text = pytesseract.image_to_string(image)

# Display the recognized text
print("\n========== RECOGNIZED TEXT ==========\n")
print(text)
print("                                         ")