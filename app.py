import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ('+5512981513149','+5512988297175')

# while len(contatos) >= 1:
    # pywhatkit.sendwhatmsg(contatos[1],'teste bot python,não responder',datetime.now().hour,datetime.now().minute + 1)
    # del contatos[1]
    # time.sleep(60)
    # keyboard.press_and_release('ctrl + w')

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[1],'nem acredito que funcionou kkkk',datetime.now().hour,datetime.now().minute + 1)
    del contatos[1]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
