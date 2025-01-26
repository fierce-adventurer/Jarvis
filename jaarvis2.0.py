import pyttsx3 as pt #text data into speech
import datetime
import speech_recognition as sr
import smtplib
from secrets_1 import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import nltk
from nltk.tokenize import word_tokenize





engine = pt.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello human, i am jarvis, your personal assistant")
    elif voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello human, i am friday, your personal assistant")
    
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)
def greeting():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good morning Human")
    elif hour >= 12 and hour <17:
        speak("afternoon human")
    elif hour>=17 and hour < 24:
        speak("Good evening human")
    else:
        speak("good night human")
def wishme():
    speak("Welcome Back human!")
    time()
    date()
    greeting()
    speak("Jaarvis at your service , please tell me how may i help you?")
    
#while True:
 #   voice = input("enter 1 for male voice and 2 for female voice \n ")
  #  speak(audio)
   # getvoices(voice)
#time()
#date()

def takeCommandCMD():
    query = input("please tell how may i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("please kindly repeat...")
        return "None"
    return query

def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    email = EmailMessage()
    email['From']= senderemail
    email['To'] = reciever
    email['subject']= subject
    email.set_content(content)
    email.send_message(email)

    server.close()

def send_whatsapp_msg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def search_google():
    speak("what do you want to search?")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='6a875544e554815878d4e938968bf19')
    speak=("what do you want to know about?")
    topic =takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,language='en',country='in',page_size=  5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x} {y["description"]}')
        speak(f'{x} {y["description"]}')

    speak("these are the top headlines for today")

def text2speech():
    speak("what do you want me to speak?")
    text = takeCommandMic()
    print(text)
    speak(text)

def screenshot():
    name_img=tt.time()
    
    name_img = f'C:\\Users\\username\\Desktop\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def password_generator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    speak(newpass)

def flip():
    speak("what do you want to flip? , a coin")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and it is"+toss)

def roll_a_die():
    speak("yes sir rolling the die")
    die = ['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("i rolled the die and it is"+roll)


    
if __name__ == "__main__":
    #getvoices(1)
    #wishme()
    wakeword = "jarvis"
    while True:

        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'email' in query:
                email_list ={
                    'test email':xyz@gmail.com
                }
                try:
                    speak("To whom you want to send email?")
                    name = takeCommandMic()
                    reciever = email_list[name]
                    speak("what is the subject of mail?")
                    subject=takeCommandMic()
                    sendEmail(reciever,subject,content)
                    speak('what should i say?')
                    content = takeCommandMic()
                    sendEmail(content)
                    speak("email has been send")
                except Exception as e:
                    print(e)
                    speak("unable to send email")

            elif 'message' in query:
                user_name = {
                    'Jarvis' : '+91 YOUR_NAME'
                }
                try:
                    speak("To whom you want to whatsapp message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("what is the message?")
                    message=takeCommandMic()
                    send_whatsapp_msg(phone_no,message)
                    speak('message has been send')
                    
                except Exception as e:
                    print(e)
                    speak("unable to send message")

            elif 'wikipedia' in query:
                speak("searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)

            elif 'search' in query:
                search_google()

            elif 'youtube' in query:
                speak("what do you want to search?")
                search = takeCommandMic()
                
                pywhatkit.playonyt(search)

            elif 'news' in query:
                news()

            elif 'read' in query:
                text2speech()

            elif 'open' in query:
                os.system('explorer C:\\{}'.format(query.replace('open','')))

            elif 'open code' in query:
                codePath = "C:\\Users\\username\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'screenshot' in query:
                screenshot()

            elif 'remember' in query:
                speak("what should i remember?")
                data = takeCommandMic()
                speak("you said me to remember"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("you said me to remember that"+remember.read())

            elif 'password' in query:
                password_generator()

            elif 'flip' in query:
                flip()

            elif 'roll' in query:
                roll_a_die()
            
            elif 'offline' in query:
                quit()

            else:
                break


