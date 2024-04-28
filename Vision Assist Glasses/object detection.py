import cv2
import imutils
import numpy as np
from imutils.video import VideoStream, FPS
import pyttsx3
import time

# Function to start object detection
def start_detection():
    prototxt_path = "classs.prototxt.txt"
    model_path = "train.caffemodel"
    start_detection_with_files(prototxt_path, model_path)

# Function to start object detection with specific files
def start_detection_with_files(prototxt_path, model_path):
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    fps = FPS().start()

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.2:
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

                if idx == 15:
                    print("human")
                    speak("HUMAN")
                elif idx == 7:
                    print("car")
                    speak("car")
                elif idx == 12:
                    print("dog")
                    speak("dog")
                elif idx == 6:
                    print("bus")
                    speak("bus")
                else:
                    print("nothing detected")

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        fps.update()

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()

# Function for speech synthesis
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate', 120)  # 120 words per minute
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

# List of classes and colors
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Start object detection directly
start_detection()
