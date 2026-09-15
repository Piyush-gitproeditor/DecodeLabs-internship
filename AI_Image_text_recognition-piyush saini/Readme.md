# Basic Image Text Recognition using OCR

## Project Overview

This project implements a basic Optical Character Recognition (OCR) system
that extracts machine-readable text from an input image.

The system uses OpenCV for image processing and Tesseract OCR for text
recognition. Image preprocessing techniques such as grayscale conversion
and adaptive thresholding are applied before OCR.

## Technologies Used

- Python
- OpenCV
- Pytesseract
- Tesseract OCR

## Project Workflow

Input Image
    ↓
Image Loading using OpenCV
    ↓
Grayscale Conversion
    ↓
Adaptive Thresholding
    ↓
Tesseract OCR
    ↓
Recognized Text
    ↓
OCR Confidence Calculation
    ↓
80% Confidence Validation
    ↓
Output Files

## Features

- Loads an input image using OpenCV
- Converts the image to grayscale
- Applies adaptive thresholding
- Extracts text using Tesseract OCR
- Calculates an overall OCR confidence score
- Validates the result against an 80% confidence threshold
- Saves the extracted text to a text file
- Generates an annotated image with detected text regions
- Saves intermediate preprocessing results

## Output

The program generates the following files:

- `gray.png` — grayscale version of the input image
- `threshold.png` — adaptively thresholded image
- `extracted_text.txt` — recognized text
- `annotated_output.png` — image with detected text regions

## Project Structure

```text
AI_Image_text_recognition-piyush saini/
│
├── input/
│   └── printed.png
│
├── output/
│   ├── gray.png
│   ├── threshold.png
│   ├── extracted_text.txt
│   └── annotated_output.png
│
├── main.py
├── requirements.txt
└── README.md