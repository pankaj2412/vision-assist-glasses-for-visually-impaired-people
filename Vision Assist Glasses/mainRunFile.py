import subprocess
import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)  # Adjust the timeout value as needed

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def run_script(command):
    if command == "object":
        print("Running object.py")
        subprocess.run(["python", "object detection.py"], check=True)
    elif command == "ocr":
        print("Running speachocr.py")
        subprocess.run(["python", "speachocr.py"], check=True)
    elif command == "exit":
        print("Exiting the program.")
        exit()

if __name__ == "__main__":
    while True:
        command = listen_for_command()

        if command:
            run_script(command)
