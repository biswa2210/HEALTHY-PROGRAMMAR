#HEALTHY PROGRAMMAR
#WATER N GLASS AFTER N SEC
#ERERCISE AFTER N SEC
#EYE EXERCISE N SEC
from datetime import datetime
from time import time
def hts(h):
    hs=h*60*60
    return hs
def mts(h):
    s=h*60
    return s
print("\n-------------------------------------------->\n<---SETUP DETAILS FOR GOOD HEALTH----------->\n-------------------------------------------->")
g=input("ENTER HOW MANY GLASS YOU WANT TO DRINK :  ")
g=str(g)
print("<----SETUP YOUR UNIT---------->\n1-->min\n2-->hr\n3-->sec")
choice=int(input("Enter your unit :: "))
if choice==1:
    t1=int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO DRINK :  "))
    init_wat=time()
    watersec=mts(t1)
    t2 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE :  "))
    init_ex = time()
    exersec = mts(t2)
    t3 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE FOR EYES :  "))
    init_eyex = time()
    eyexersec = mts(t3)
elif choice == 2:
        t1 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO DRINK :  "))
        init_wat = time()
        watersec = hts(t1)
        t2 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE :  "))
        init_ex = time()
        exersec = hts(t2)
        t3 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE FOR EYES :  "))
        init_eyex = time()
        eyexersec = hts(t3)
elif choice == 3:
            t1 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO DRINK :  "))
            init_wat = time()
            watersec =t1
            t2 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE :  "))
            init_ex = time()
            exersec = t2
            t3 = int(input("ENTER HOW MUCH TIME AFTER YOU WANT TO EXERCISE FOR EYES :  "))
            init_eyex = time()
            eyexersec = t3
else:
    print("INVALID INPUT")

def mylogs(sms):
    with open("healthlog.txt","a") as fp:
        fp.write(f"{sms} {datetime.now()}\n")
from pygame import mixer
def playmusic(file,stopper):
    while True:
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        a=input("type 'stop' to stop playing :: ")
        if a==stopper:
            mixer.music.stop()
            break

while True:
    if time() - init_wat > watersec:
        print(f"\nThis is the time to drink water({g} glass)...hurry up...\n")
        playmusic("water.mp3","stop")
        init_wat=time()
        mylogs("Drank at ")
    elif time() - init_ex >exersec:
        print("\nThis is the time to physical exercise...hurry up...\n")
        playmusic("exercise.mp3","stop")
        init_ex=time()
        mylogs("Physical Exercise at ")
    elif time() - init_eyex >eyexersec:
        print("\nThis is the time to exercise for eyes...hurry up...\n")
        playmusic("eyeexercise.mp3","stop")
        init_eyex=time()
        mylogs("Eye Exercise at ")