import json
from const import *
with open(SettingsDataPATH, 'rt') as f:
    data = json.load(f)





URL = data['URL']
FPS = data['FPS']
MYPORT = data['myPORT']
if FPS < 30:
    RPS = FPS
else:
    RPS = 30

NAME = data['name']
WIDTH = data['width']
HEIGHT = data['height']
BACKGROUNDCOLOR = 'black'
