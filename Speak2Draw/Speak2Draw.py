import speech_recognition as sr
import turtle

r = sr.Recognizer()

canvas = turtle.Screen()
canvas.title("Speak2Draw: A Voice-Activated Image Creator")
canvas.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(3)

def process_command(command):
    if command == "draw a line":
        pen.forward(100)
    elif command == "add a snake":
        pen.circle(50)
    else:
        print("Command not recognized.")

def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("Command:", command)
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print("Speech recognition request failed:", str(e))

while True:
    listen_for_commands()
turtle.done()
