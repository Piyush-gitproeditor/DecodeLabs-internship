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
#text = pytesseract.image_to_string(image)
data= pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
print("\n============OCR RESULTS============\n")
t_confidence=0
count =0
for i in range(len(data["text"])):
    word= data["text"][i].strip()
    confidence = float(data["conf"][i])

    if word != "" and confidence >=0:
        print(word," confidence:",confidence)
        t_confidence += confidence
        count +=1

if count>0:
    avg_confidence = t_confidence/count
    print("\n Average confidence:", round(avg_confidence,2),"%")

    if avg_confidence>=80:
        print("Status: Pass")
    else:
        print("Status : Below 80%")

# Display the recognized text
print("\n========== RECOGNIZED TEXT ==========\n")
print(text)
print("                                         ")