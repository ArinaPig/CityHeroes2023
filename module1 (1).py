import tkinter as tk
from PIL import ImageTk
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr

def del1():
    t1['state'] = tk.NORMAL
    t1.delete(1.0, 'end')
    t1['state'] = tk.DISABLED
    lis1 = 1
    lis2 = []
    r = sr.Recognizer()
    l1 = list()
    l2 = list()

    def listen():
        with sr.Microphone() as source:
            print('-----------------')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='ru-RU')
                t = text
            except sr.UnknownValueError:
                pass
            print(text)
            return t;

    while lis1 == 1:
        l1=listen()
        print(l1)
        if len(l1.split()) > 4:
            l2.append(l1)
        lab1['text'] = l2



def stih():
    t1['state'] = tk.NORMAL
    url_main = "https://rustih.ru/aleksandr-pushkin/"

    response_main = requests.get(url_main)

    soup = BeautifulSoup(response_main.text, "lxml")

    data = soup.find("div", class_="post-card-one")

    name = data.find("div", class_="entry-title").text.replace("\n", "")

    url_sub = data.find("a").get("href")

    response_sub = requests.get(url_sub)

    soup2 = BeautifulSoup(response_sub.text, "lxml")

    text = soup2.find("div", class_="entry-content poem-text").text

    t1.insert(1.0, text)
    t1['state'] = tk.DISABLED



root = tk.Tk()

root.geometry('1300x450+900+100')

e = tk.Entry(root, width=20)
e.place(x=160, y=50)

b2 = tk.Button(root, text='Найти', command=stih)
b2.place(x=300, y=50)


t1 = tk.Text(root, width=50, height=15, bg='lightgrey', state=tk.DISABLED)
t1.place(x=160, y=85)

scroll = tk.Scrollbar(command=t1.yview)
scroll.place(x=560, y=85, height=245)

t1.config(yscrollcommand=scroll.set)

lab1 = tk.Label(bg='grey', width=100, height=15 )
lab1.place(x=590, y=90)

image = ImageTk.PhotoImage(file="knopka3.png")
tk.Button(root, image=image, command=del1).place(x=15, y=140)


lab3 = tk.Label(bg='grey', text="Выделение:", font='Times 13', height=3, width=9)
lab3.place(x=590, y=90)

root.mainloop()
