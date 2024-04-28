import cv2
import pytesseract
from gtts import gTTS
import os
import time

# Set the path to the Tesseract OCR executable (update this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def recognize_and_speak(frame):
    # Convert the frame to grayscale for OCR
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use OCR to recognize text
    text = pytesseract.image_to_string(gray_frame).strip()

    # Print the recognized text
    print("Recognized Text:", text)

    # Check if there is text before converting to speech
    if text:
        # Convert the recognized text to speech
        tts = gTTS(text=text, lang='en')

        # Save the speech as an audio file
        tts.save("output.mp3")

        # Play the saved audio file
        os.system("start output.mp3")
    else:
        print("No text to speak")

def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Set the time interval for capturing images (5 seconds)
    capture_interval = 3

    while True:
        # Capture video frame
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Wait for 5 seconds
        time.sleep(capture_interval)

        # Perform OCR and speak the text
        recognize_and_speak(frame)

        # Break the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
