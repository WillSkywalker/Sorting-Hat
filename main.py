#!/usr/bin/env python

import tkinter as tk
import pyaudio
import wave
import threading
from PIL import Image, ImageTk
from functools import partial
from string import ascii_uppercase
from sorting_hat.hat import Hat, IllegalAnswerError, answer_map

def play_hedwig_theme():
    wf = wave.open('resources/hp.wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    while True:

        wf.setpos(0)
        data = wf.readframes(1024)

        while data:
            stream.write(data)
            data = wf.readframes(1024)


class SortingHatGUI(tk.Tk):

    def __init__(self, hat):
        super(SortingHatGUI, self).__init__()
        self.hat = hat
        self.title('分院帽')
        self.configure(bg='#000000')

        title_image = ImageTk.PhotoImage(Image.open('resources/hat.jpg'))
        banner = tk.Label(self, image=title_image)
        banner.image = title_image
        banner.grid(columnspan=3)

        self.initial_screen(init=True)

        self.resizable(width=False, height=False)
        threading.Thread(target=play_hedwig_theme, daemon=True).start()


    def initial_screen(self, init=False):
        if not init:
            for button in self.buttons:
                button.destroy()
            self.label.destroy()
            self.sublabel.destroy()
            self.button_frame.destroy()
        self.label = tk.Label(text='  把我好好地扣在头上，\n  我从来没有看走过眼，\n  我要看一看你的头脑，\n  判断你属于哪个学院！',
                 bg='black', fg='white')
        self.label.grid(row=1, column=1)

        self.sublabel = tk.Label()
        self.button = tk.Button(text='开始测试', bg='black', 
            highlightbackground='black', command=self.update)
        self.button.grid(row=3, column=1)
        self.buttons = []
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(column=1)


    def update(self):
        self.button.destroy()
        question = self.hat.ask_question()
        if question is None:
            self.result()
            return
        self.label.destroy()
        self.label = tk.Label(text=question['question'], bg='black', fg='white')
        self.label.grid(row=1, column=1)
        self.sublabel.destroy()
        self.sublabel = tk.Label(text='\n'.join(question['answers']), 
                                 bg='black', fg='white')
        self.sublabel.grid(row=2, column=1)
        for button in self.buttons:
            button.destroy()
        for i in range(len(question['answers'])):
            button = tk.Button(self.button_frame, text=ascii_uppercase[i], highlightbackground='black', 
                               command=partial(self.choose_answer, answer=ascii_uppercase[i]))
            button.grid(row=0, column=i)
            self.buttons.append(button)


    def choose_answer(self, answer):
        self.hat.answer_question(answer)
        self.update()


    def result(self):
        self.label.destroy()
        self.label = tk.Label(text='您的学院是', bg='black', fg='white')
        self.label.grid(row=1, column=1)

        self.sublabel.destroy()
        self.sublabel = tk.Label(text=self.hat.calculate_house(), 
                         bg='black', fg='white', font=("", 24))
        self.sublabel.grid(row=2, column=1)
        for button in self.buttons:
            button.destroy()
        self.hat = Hat('data/questions.json')
        replay = tk.Button(self.button_frame, text='再来一次', highlightbackground='black', 
                               command=self.initial_screen)
        replay.grid()
        self.buttons.append(replay)



if __name__ == '__main__':
    your_hat = Hat('data/questions.json')
    game = SortingHatGUI(your_hat)
    game.mainloop()
