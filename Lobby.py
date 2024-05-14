from tkinter import ttk
import tkinter as tk
from threading import Thread



class Lobby:
    def __init__(self, name, conn, api):
        self.app = tk.Tk()
        self.app.geometry('500x500')
        self.app.title(f"Лобби ({name})")
        label = ttk.Label(self.app, text='Ожидаем')
        label.pack()
        btn = ttk.Button(self.app, text='Готово!', command=lambda: self.game_start(api))
        Thread(target=lambda: conn(btn)).start()

        self.app.mainloop()

    def game_start(self, api):
        print('lobby destroy')
        print('Запускаю game')
        from Game.Game import Game

        self.app.destroy()
        Game(api)



