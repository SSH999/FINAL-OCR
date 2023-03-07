# Import the required libraries
import pytesseract
import cv2

# Load the image
img = cv2.imread('')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Apply dilation to the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# Perform OCR on the image
text = pytesseract.image_to_string(dilate, lang='eng')

# Print the text
print(text)
