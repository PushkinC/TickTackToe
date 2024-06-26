from tkinter import ttk
import tkinter as tk
from const import *
import json
import os
from API.API import API
from Lobby import Lobby



def btn_click(btn):
    with open(SettingsDataPATH, 'w') as f:
        data = {
            'URL': inp_URL.get(),
            'FPS': int(inp_FPS.get()),
            'width': int(inp_width.get()),
            'height': int(inp_height.get()),
            'name': inp_name.get(),
            "myPORT": int(inp_port.get())
        }
        json.dump(data, f)

    # with open('../Saves/PlayerData.json', 'w') as f:
    #     data = {
    #         'name': inp_name.get()
    #     }
    #     json.dump(data, f)
    #
    app.destroy()
    api = API()
    match btn:
        case 0:
            pass
        case 1:
            Lobby('хост', api.CreateLobby, api)

        case 2:
            Lobby('игрок', api.ConnectToLobby, api)




if not os.path.exists(SettingsDataPATH):
    print(f"Нет файла {SettingsDataPATH}")
    print(f'Создаю файл {SettingsDataPATH}')
    f = open(SettingsDataPATH, 'w+')
    f.close()

isEmpty = False
with open(SettingsDataPATH, 'rt') as f:
    try:
        SettingsData = json.load(f)
    except json.decoder.JSONDecodeError:
        isEmpty = True
        print(f"Файл {SettingsDataPATH} пустой")
        SettingsData = {
            "URL": "192.168.255.255:0000",
            "FPS": 30,
            "width": 500,
            "height": 500,
            "name": "name",
            "myPORT": 4444
        }
    except Exception as ex:
        print(ex)
        print('Пупупу... Зовите меня!')
        exit()


app = tk.Tk()
app.geometry('500x500')
app.title("Найстрока") if not isEmpty else app.title('Настройка (пустой файл)')


frame1 = ttk.Frame(app)
frame1.pack(fill='x')

label_URL = ttk.Label(frame1, text='Введите URL:')
label_URL.pack(side=tk.LEFT, padx=5, pady=5)
inp_URL = ttk.Entry(frame1)
inp_URL.insert(0, SettingsData['URL'])
inp_URL.pack(fill='x', padx=5, expand=True)

frame2 = ttk.Frame(app)
frame2.pack(fill='x')

label_FPS = ttk.Label(frame2, text='Введите FPS:')
label_FPS.pack(side=tk.LEFT, padx=5, pady=5)
inp_FPS = ttk.Entry(frame2)
inp_FPS.insert(0, SettingsData['FPS'])
inp_FPS.pack(fill='x', padx=5, expand=True)

frame4 = ttk.Frame(app)
frame4.pack(fill='x')

label_width = ttk.Label(frame4, text='Введите ширину экрана:')
label_width.pack(side=tk.LEFT, padx=5, pady=5)
inp_width = ttk.Entry(frame4)
inp_width.insert(0, SettingsData['width'])
inp_width.pack(fill='x', padx=5, expand=True)

frame5 = ttk.Frame(app)
frame5.pack(fill='x')

label_height = ttk.Label(frame5, text='Введите высоту экрана:')
label_height.pack(side=tk.LEFT, padx=5, pady=5)
inp_height = ttk.Entry(frame5)
inp_height.insert(0, SettingsData['height'])
inp_height.pack(fill='x', padx=5, expand=True)

frame3 = ttk.Frame(app)
frame3.pack(fill='x')

label_name = ttk.Label(frame3, text='Введите имя:')
label_name.pack(side=tk.LEFT, padx=5, pady=5)
inp_name = ttk.Entry(frame3)
inp_name.insert(0, SettingsData['name'])
inp_name.pack(fill='x', padx=5, expand=True)

frame6 = ttk.Frame(app)
frame6.pack(fill='x')

label_name = ttk.Label(frame6, text='Введите ваш порт')
label_name.pack(side=tk.LEFT, padx=5, pady=5)
inp_port = ttk.Entry(frame6)
inp_port.insert(0, SettingsData['myPORT'])
inp_port.pack(fill='x', padx=5, expand=True)

frame7 = ttk.Frame(app)
frame7.pack(fill='x')

save_btn = ttk.Button(frame7, command=lambda: btn_click(0))
save_btn['text'] = 'Сохранить'
save_btn.pack(fill='x', side=tk.LEFT, padx=5, pady=5)

save_and_start_btn = ttk.Button(frame7, command=lambda: btn_click(1))
save_and_start_btn['text'] = 'Сохранить и запустить лобби'
save_and_start_btn.pack(fill='x', side=tk.RIGHT, padx=5, pady=5)

save_and_connect_btn = ttk.Button(frame7, command=lambda: btn_click(2))
save_and_connect_btn['text'] = 'Сохранить и подключиться'
save_and_connect_btn.pack(fill='x', side=tk.RIGHT, padx=5, pady=5)

app.mainloop()

