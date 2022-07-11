from datetime import datetime
import time
import os
from pygame import mixer
def mylogs(sms):
    with open("drank_water_chart.txt","a") as fp:
        fp.write(f"{sms} {time.asctime(time.localtime((time.time())))}\n")
def playmusic(file,stopper):
    while True:
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        a=input("type 'stop' to stop playing :: ")
        if a==stopper:
            mixer.music.stop()
            break
g=input("ENTER HOW MANY GLASS YOU WANT TO DRINK :  ")
g=str(g)
min=0
sec=0
ming = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO DRINK (min):  "))
while True:
    time.sleep(1)
    sec=sec+1;
    if(sec==59):
        sec=0
        min=min+1
    if min==ming:
        print(f"\nThis is the time to drink water({g} glass)...hurry up...\n")
        playmusic("water.mp3","stop")
        min=0
        mylogs("Drank at ")