import ssl
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from mimetypes import guess_type
from playsound import playsound
import speech_recognition as sr
import smtplib
import pyaudio
from bs4 import BeautifulSoup
import email
from email import policy, encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email import message
import imaplib
from gtts import gTTS
import pyglet
import os, time
from tkinter import ttk
from tkinter import *
import socket
IPaddress=socket.gethostbyname(socket.gethostname())


user=''
pwd = ''
recemail = ''


win= Tk()
win.geometry("700x350")
Label(win, text= "Welcome To Voice Based Email System", font= ('Aerial 17 bold italic')).pack(pady= 30)

def add_label(txt):
   global label
   label=Label(win, text=txt, font=('Aerial 10 bold italic'),fg="#034f84").place(x=150,y=150)


def login(user,pwd):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    try:
        mail.login(user, pwd)
        user=user
        speakit("Login successful")
        print("login succesful")
        return True

    except:
        speakit("Login failed..")

        return False

def fetchCred():

    speakit("Speak your gmail ID")


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your gmail Id:")
        audio = r.listen(source)
        print("ok done!!")
    try:
        text = r.recognize_google(audio)
        text = text.replace(' ', '')
        text = text.replace('yes', 's')
        text = text.replace('dot', '..')
        text.lower()
        print("You said: " + text + "@gmail.com")
        user = text.lower() + "@gmail.com"
        speakit("You said "+user)


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        user=" "

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        user=" "

    # recording password

    speakit("Speak your password")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Password:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text = r.recognize_google(audio)
        text = text.replace(' ', '')
        text = text.replace('are', 'r')
        text = text.replace('you', 'u')
        text.lower()

        print("You said:" + text)
        speakit("You said "+text)
        pwd = text
        return user,pwd

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        pwd=" "

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        pwd=" "

def choiceconf(user,pwd):
    speakit("Want to continue or close application. Speak yes for continue or no for close application")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text1 = r.recognize_google(audio)
        text1 = text1.lower()
        print("You said:" + text1)
        if text1 == "Yes" or text1 == "yes" or text1 == "YES" or text1 == "s" or text1 == "S" or text1 == "yash":
            getchoice(user, pwd)
        else:
            speakit("Thanks for using Voice Based Email Application.")
            win.destroy()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        speakit("Thanks for using Voice Based Email Application.")
        win.destroy()

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speakit("Thanks for using Voice Based Email Application.")
        win.destroy()

def sendMail(user,pwd):
    speakit("speak receiver's email id")
    gmail=''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text1 = r.recognize_google(audio)
        text1 = text1.replace(' ', '')
        text1 = text1.replace('yes', 's')
        text1 = text1.replace('dot', '..')
        text1.lower()
        print("You said:" + text1.lower() + "@gmail.com")
        gmail = text1 + "@gmail.com"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    speakit("Speak Subject:")
    r = sr.Recognizer()  # recognize
    with sr.Microphone() as source:
        print("Your subject :")
        audio = r.listen(source)
        print("ok done!!")
    try:
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        sub = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    speakit("Speak Body Message:")
    r = sr.Recognizer()  # recognize
    with sr.Microphone() as source:
        print("Your message :")
        audio = r.listen(source)
        print("ok done!!")
    try:
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        body = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    message = MIMEMultipart()
    message["From"] = user
    message["To"] = gmail
    message["Subject"] = sub
    message["Bcc"] = gmail

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    msg = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, pwd)
        server.sendmail(user, gmail, msg)
    print("Congrates! Your mail has send. ")
    speakit("Congrates! Your mail has send.")
    choiceconf(user,pwd)



def sendAttemail(user,pwd):
    speakit("speak receiver's email id")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text1 = r.recognize_google(audio)
        text1 = text1.replace(' ', '')
        text1 = text1.replace('yes', 's')
        text1 = text1.replace('dot', '..')
        text1.lower()
        print("You said:" + text1.lower() + "@gmail.com")
        gmail = text1 + "@gmail.com"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    speakit("Speak Subject:")
    r = sr.Recognizer()  # recognize
    with sr.Microphone() as source:
        print("Your subject :")
        audio = r.listen(source)
        print("ok done!!")
    try:
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        sub = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    speakit("Speak Body Message:")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your message :")
        audio = r.listen(source)
        print("ok done!!")
    try:
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        body = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    message = MIMEMultipart()
    message["From"] = user
    message["To"] = gmail
    message["Subject"] = sub
    message["Bcc"] = gmail

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "file.txt"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    msg = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, pwd)
        server.sendmail(user, gmail, msg)
    print("Congrates! Your email with an attachment has send. ")
    speakit("Congrates! Your email with an attachment has send.")
    choiceconf(user,pwd)


def speakit(t):
    tts = gTTS(text=t, lang='en')
    ttsname = ("name.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

def readMail(user,pwd):
    flag=True
    imap_url = 'imap.gmail.com'
    conn = imaplib.IMAP4_SSL(imap_url)
    conn.login(user, pwd)
    conn.select('"INBOX"')
    result, data = conn.search(None, '(UNSEEN)')
    unread_list = data[0].split()
    no = len(unread_list)
    result1, data1 = conn.search(None, "ALL")
    mail_list = data1[0].split()
    text = "You have reached your inbox. There are " + str(
        len(mail_list)) + " total mails in your inbox. You have " + str(
        no) + " unread emails" + ". To read unread emails say unread. To search a specific email say search."
    speakit(text)
    while (flag):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Your choice:")
            audio = r.listen(source)
            print("ok done!!")

        try:
            act = r.recognize_google(audio)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            speakit("Error")
            getchoice(user,pwd)

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            speakit("Error")
            getchoice(user,pwd)
        act = act.lower()
        print(act)
        if act == 'unread':
            flag = False
            if no != 0:
                red(unread_list, 'inbox',conn)
            else:
                print("You have no unread emails.")
        elif act == 'search':
            flag = False
            mailid = ""
            while True:
                print("Enter email ID of the person who's email you want to search.")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Your choice:")
                    audio = r.listen(source)
                    print("ok done!!")

                try:
                    emailid = r.recognize_google(audio)

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                    speakit("Error")
                    getchoice(user, pwd)



                speakit("You meant " + emailid + " say yes to confirm or no to enter again")

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Your choice:")
                    audio = r.listen(source)
                    print("ok done!!")

                try:
                    yn = r.recognize_google(audio)

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                    speakit("Error")
                    getchoice(user, pwd)

                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    speakit("Error")
                    getchoice(user, pwd)
                yn = yn.lower()
                if yn == 'yes':
                    break
            emailid = emailid.strip()
            emailid = emailid.replace(' ', '')
            emailid = emailid.lower()
            emailid = emailid + "@gmail.com"
            search_specific_mail('INBOX', 'FROM', emailid, 'inbox',mail_list)

        elif act == 'back':
            getchoice(user,pwd)

            conn.logout()

    choiceconf(user,pwd)
def red(mail_list,folder,conn):
    global s, i
    mail_list.reverse()
    mail_count = 0
    to_read_list = list()
    for item in mail_list:
        result, email_data = conn.fetch(item, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        speakit("Email number " + str(mail_count + 1) + "   . The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject)
        speakit('message id= ', Msg_id)
        speakit('From :', From)
        speakit('To :', To)
        speakit('Subject :', Subject)
        print("\n")
        to_read_list.append(Msg_id)
        mail_count = mail_count + 1


    flag = True
    while flag :
        n = 0
        flag1 = True
        while flag1:
            speakit("Enter the email number of mail you want to read.")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Your choice:")
                audio = r.listen(source)
                print("ok done!!")

            try:
                n = r.recognize_google(audio)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
                speakit("Error")
                getchoice(user, pwd)

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                speakit("Error")
                getchoice(user, pwd)
            print(n)
            speakit("You meant " + str(n) + ". Say yes or no.")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Your choice:")
                audio = r.listen(source)
                print("ok done!!")

            try:
                say = r.recognize_google(audio)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
                speakit("Error")
                getchoice(user, pwd)

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                speakit("Error")
                getchoice(user, pwd)
            say = say.lower()
            if say == 'yes':
                flag1 = False
        n = int(n)
        msgid = to_read_list[n - 1]
        speakit("message id is =", msgid)
        typ, data = conn.search(None, '(HEADER Message-ID "%s")' % msgid)
        data = data[0]
        result, email_data = conn.fetch(data, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']

        speakit("To :"+ To+"Subject :"+Subject+'From :'+ From,"The mail is from " +From + " to " + To + "  . The subject of the mail is " + Subject)
        #uBody = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        if Body != '':
            print(Body)
        else:
            print("Body is empty.")
def search_specific_mail(folder, key, value, foldername,mail_list):
    global i, conn
    conn.select(folder)
    result, data = conn.search(None, key, '"{}"'.format(value))

    if len(mail_list) != 0:
        speakit("There are " + str(len(mail_list)) + " emails with this email ID.")

    if len(mail_list) == 0:
        speakit("There are no emails with this email ID.")
    else:
        red(mail_list, foldername)

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

def getchoice(user,pwd):
    print("1. composed a mail.")
    add_label("option 1. Compose a Simple email.")
    speakit("option 1. Compose a Simple email.")

    print("2. Compose a email with an attachment")
    add_label("option 2. Compose a email with an attachment")
    speakit("option 2. Compose a email with an attachment")

    print("3. Check your inbox")
    add_label("option 3. Check your inbox")
    speakit("option 3. Check your inbox")

    speakit("Your choice")
    text=''

    # voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")
        speakit("OK")

    try:
        text = r.recognize_google(audio)
        text='3'
        print("You said : " + text)
        speakit("You said "+text)



    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        text='3'

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text='3'

    #   choices details
    if text == '1' or text == 'One' or text == 'one' or text == 'van':
        sendMail(user,pwd)

    elif text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To':
        sendAttemail(user,pwd)

    elif text == 'three' or text == 'tree' or text == '3':
        readMail(user,pwd)
    else:
        speakit("Choice couldn't recognized. want speak choice again or close Application. Say yes for Choice and No for Close Application")
        comfirmation("n")


def comfirmation(txt):
    speakit("Speak")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text = r.recognize_google(audio)
        text=text.lower()
        print("You said : " + text)

        if text == "Yes" or text == "yes" or text == "YES" or text == "s" or text == "S" or text=="yash":
            if txt=="s":
                start_it()
            else:
                getchoice(user,pwd)
        else:
            speakit("Thanks for using Voice Based Email Application.")
            win.destroy()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        speakit("Error")
        win.destroy()

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speakit("Error")
        win.destroy()


def start_it():
    #user,pwd=fetchCred()

    s=login("sargamss2002@gmail.com","bkamrgeobkpbtqwn")
    if s==True:
        getchoice("sargamss2002@gmail.com","bkamrgeobkpbtqwn")

    else:

        speakit("Want to login again or Close Application. Say Yes for Login Again and No for Close Application.")
        comfirmation("s")


def strt():

    if IPaddress == "127.0.0.1":
        print("No internet, your localhost is "
              ""
              "" + IPaddress)
        playsound('note.mp3')
        win.destroy()
    else:
        print("Connected, with the IP address: " + IPaddress)
        speakit("Project: Voice based Email System")
        start_it()


ttk.Button(win, text= "Start", command=strt).pack(pady= 20)
win.mainloop()