from pdfminer.high_level import extract_text
import pyttsx3
from tkinter import *
from tkinter import filedialog, simpledialog


window = Tk()
window.geometry('500x500')
window.resizable(width=True,height=True)
window.title('Pdf to Speech')

text = ''

def set_path():
    filename = filedialog.askopenfilename(title='Open')
    return filename

def load_file():
    global text
    x = set_path()
    text = extract_text(x)
    w.insert(1.0,text)

def read_file():
    text_to_speech = w.get("1.0",END)
    engine = pyttsx3.init()
    engine.say(text_to_speech)
    engine.runAndWait()


find_file = Button(window, text='Select File', command=load_file)
find_file.pack()

read_file_btn = Button(window, text='Read File', command=read_file)
read_file_btn.pack()

w = Text(window)
w.pack()

window.mainloop()