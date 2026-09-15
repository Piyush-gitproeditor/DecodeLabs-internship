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
cv2.imwrite("output/gray.jpg", gray)
print ("grayscale image created successfully")

# Apply threshold 
threshold = cv2.adaptiveThreshold (gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,11)
cv2.imwrite("output/threshold.jpg", threshold)
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
# Create a copy of the original image
annotated = image.copy()

# Draw bounding boxes around detected text
for i in range(len(data["text"])):

    word = data["text"][i].strip()
    confidence = float(data["conf"][i])

    if word != "" and confidence >= 0:
        confidences.append(confidence)

# Save annotated image
cv2.imwrite("output/annotated_output.png", annotated)

print("Annotated image saved to output/annotated_output.png")

# Display the recognized text
print("\n========== RECOGNIZED TEXT ==========\n")
print(text)
# Save recognized text to a file
with open("output/extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nRecognized text saved to output/extracted_text.txt")
print("                                         ")
