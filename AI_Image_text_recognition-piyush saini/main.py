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

#apply grayscale 
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)
print ("grayscale image created successfully")

# Apply threshold 
threshold = cv2.adaptiveThreshold (gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,11)
cv2.imwrite("threshold.jpg", threshold)
print("Adaptive threshold image created Successfully")
# Perform OCR
text = pytesseract.image_to_string(threshold)
data= pytesseract.image_to_data(threshold, output_type=pytesseract.Output.DICT)
print("\n============OCR RESULTS============\n")
confidences=[]
for confidence in data["conf"]:
    confidence = float(confidence)

    if confidence >=0:
        confidences.append(confidence)

if confidences:
    avg_confidence = sum(confidences)/ len(confidences)
    print("\n Average confidence:", round(avg_confidence,2),"%")

    if avg_confidence>=80:
        print("Status: Pass")
    else:
        print("Status : Below 80%")

# Display the recognized text
print("\n========== RECOGNIZED TEXT ==========\n")
print(text)
print("                                         ")
