import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

listener = sr.Recognizer( )
alexa = pyttsx3.init()

def talk(text): 
    alexa.say(text)
    alexa.runAndWait()    

def take_command( ): 
    try:
        with sr.Microphone() as source:
            print("listening...") 
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
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
          
        
        

run_alexa() 