import cv2
import os
from cvzone.FaceDetectionModule import FaceDetector
from datetime import datetime

# Create a folder to save screenshots if it doesn't exist
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

def save_screenshot(img):
    # Generate a unique filename based on the current time
    filename = os.path.join(screenshot_folder, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    cv2.imwrite(filename, img)
    print(f"Screenshot saved: {filename}")

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    if not success:
        break

    # Returns bounding boxes for the face
    img, bBoxes = detector.findFaces(img)

    # If a face is detected, take a screenshot
    if bBoxes:
        save_screenshot(img)

    # Add the text overlay with red color
    cv2.putText(img, 'FATIMA <3', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()