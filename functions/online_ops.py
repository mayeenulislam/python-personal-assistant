import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address['ip']

def search_wikipedia(query):
    return wikipedia.summary(query, sentences=2)

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_msg(number, message):
    kit.sendwhatmsg_instantly(f"+88{number}", message)


EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

def send_email(receiver_address, subject, message):
    try:
        email: EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
