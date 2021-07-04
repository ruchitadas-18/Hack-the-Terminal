#     Megabot
#     Team CYBERNOIDS


#libraries
import smtplib
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
from instapy import InstaPy
from instapy import smart_run
from happy import talk
from email.message import EmailMessage
import time

#Whatsappbot

def what():
    from happy1 import talk
    def talk(text):
        talk()
    from os import startfile

    from pyautogui import click
    from keyboard import press
    from keyboard import write
    from time import sleep


    def WhatsappMsg(name, message):
        sleep(20)
        startfile("C:\\Users\\Parth Agrawal\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        sleep(5)

        click(x=624, y=736)

        sleep(1)

        write(name)

        sleep(1)
        click(x=659, y=705)

        sleep(1)
        click(x=1142, y=615)

        sleep(1)

        write(message)

        press('enter')


    WhatsappMsg('kartik', '2nd try.')

#Mailbot

def mail():

    listener = sr.Recognizer()
    engine = pyttsx3.init()

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def get_info():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                print(info)
                return info.lower()

        except:
            pass


    def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('happyagrawal120@gmail.com', 'Ha@120802')
        email = EmailMessage()
        email['From'] = 'happyagrawal120@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)

    # Give your list of names and their respective Emails here

    email_list = {
        'parth':'agrawalparth564@gmail.com',
        'pranav':'agrawalpranav71@gmail.com',
        'papa':'parthagrawal35976@gmail.com',
        'kartik': "kartiks914@gmail.com"
    }

    def get_email_info():
        print("To whom you want to send mail")
        talk('To whom you want to send mail')
        name = get_info()
        receiver = email_list[name]
        print(receiver)
        print("What is the subject of your mail")
        talk('What is the subject of your mail')
        subject = get_info()
        print('Tell the message of your mail')
        talk('Tell the message of your mail')
        message = get_info()


        send_email(receiver, subject, message)

        talk('Hey man. Your mail is sent')
        talk('Do you want to send more mails')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()


    get_email_info()


#TelegramBot

def Tel():
    from happy3 import talk
    def talk(text):
        talk()

    class BotHandler:
        def __init__(self, token):
                self.token = token
                self.api_url = "https://api.telegram.org/bot{}/".format(token)

        def get_updates(self, offset=0, timeout=30):
            method = 'getUpdates'
            params = {'timeout': timeout, 'offset': offset}
            resp = requests.get(self.api_url + method, params)
            result_json = resp.json()['result']
            return result_json

        def send_message(self, chat_id, text):
            params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
            method = 'sendMessage'
            resp = requests.post(self.api_url + method, params)
            return resp

        def get_first_update(self):
            get_result = self.get_updates()

            if len(get_result) > 0:
                last_update = get_result[0]
            else:
                last_update = None

            return last_update


    token = '1818066897:AAEN8bMeIJJnAkBUJC8SWZwJPyANeOf8Q2I' #Token of your bot
    mnb1321_bot = BotHandler(token)

    def main():
        new_offset = 0
        print('hi, now launching...')

        while True:
            all_updates=mnb1321_bot.get_updates(new_offset)

            if len(all_updates) > 0:
                for current_update in all_updates:
                    print(current_update)
                    first_update_id = current_update['update_id']
                    if 'text' not in current_update['message']:
                        first_chat_text='New member'
                    else:
                        first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    if 'first_name' in current_update['message']:
                        first_chat_name = current_update['message']['chat']['first_name']
                    elif 'new_chat_member' in current_update['message']:
                        first_chat_name = current_update['message']['new_chat_member']['username']
                    elif 'from' in current_update['message']:
                        first_chat_name = current_update['message']['from']['first_name']
                    else:
                        first_chat_name = "Sidharth"

                    if first_chat_text == 'Hi':
                        mnb1321_bot.send_message(first_chat_id, 'Morning ' + first_chat_name)
                        new_offset = first_update_id + 1
                    else:
                        mnb1321_bot.send_message(first_chat_id, 'We are CYBERNOIDS'+first_chat_name)
                        new_offset = first_update_id + 1


    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            exit()

# InstagramBot

def insta():
    from happy2 import talk
    def talk(text):
        talk()
    # login credentials
    insta_username = 'insta_.bot'
    insta_password = 'Hacker.001'

    comments = ['Nice shot! @{}',
                'I love your profile! @{}',
                'Your feed is an inspiration :thumbsup:',
                'Just incredible :open_mouth:',
                'What camera did you use @{}?',
                'Love your posts @{}',
                'Looks awesome @{}',
                'Getting inspired by you @{}',
                ':raised_hands: Yes!',
                'I can feel your passion @{} :muscle:']

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)

    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_dont_include(["friend1", "friend2", "friend3"])

        # activity
        session.like_by_tags(["geeksforgeeks"], amount=10)

        # Joining Engagement Pods
        session.set_do_comment(enabled=True, percentage=35)
        session.set_comments(comments)
        session.join_pods(topic='sports', engagement_mode='no_comments')

        session.set_do_follow(enabled=True, percentage=10, times=2)
        users = session.target_list("C:\\Users\\Parth Agrawal\\users.txt")
        session.follow_user_followers(users, amount=10, randomize=True)

def talk(text):
  talk()
print("***************************")
print("Hello!! Welcome to MegaBot\n")
print("***************************")
print ("Instagram")
print("Telegram")
print("Mail")
print("Whatsapp")
print("***************************")
abc = """
    (._.)
    Which social platform do you want to access ?
    listening....  
"""
options = int(input(abc))

if (options==1):
    insta()
elif (options==2):
    Tel()
elif (options==3):
    mail()
elif (options==4):
    print("to whom do you want to send message")
    print("listening......")


    what()

else:
    print("(._.)")


# Thankyou

#  MegaBot : "Please use my MiniBots"
#  Team CYBERNOIDS












