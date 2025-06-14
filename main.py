import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer( )
alexa = pyttsx3.init()

def talk(text): 
    alexa.say(text)
    alexa.runAndWait()    

def take_command(): 
    command = ""    
    try:
        with sr.Microphone() as source:
            print("listening...") 
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")  
    except:
        pass
    return command
# if ask time anyone alexa tall time now 
def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p") 
        print(time)  
        talk("current time is" + time) 
        # play song  
    elif "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song) 
          
    elif "tell me about" in command: 
            look_for = command.replace("tell me about", "")  
            info = wikipedia.summary(look_for, 1)
            print(info) 
            talk(info)
            
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("sorry, I cannot hear you. but i search in for you")
        pywhatkit.search(command)

while True:
    run_alexa() 