import random
from pygame import mixer
import time
from datetime import datetime
def Playmusic(Music):
    mixer.init()
    mixer.music.load(Music)
    mixer.music.play()
Playmusic("Sunny.mp3")
print("Note that Input provided should be in CAPITAL LETTERS only.")
print("$$$$$$$$ You have to complete this Game within 2.5 minutes to complete $$$$$$$$")
print("Let's start the GAME......")
Hollywood = ["IRONMAN", "BATMAN", "HARRYPOTTER", "SPIDERMAN", "REDNOTICE", "JUNGLEBOOK", "BATTLESHIP", "AVATAR",
             "AVENGERS", "JOKER", "MATRIX", "JUNGLECRUISE", "GLADIATOR", "TAXIDRIVER", "TENET", "ANTMAN", "FREEGUY",
             "GODFATHER", "INCEPTION", "INTERSTELLER", "TERMINATOR", "PIANIST", "PRESTIGE", "DEPARTED", "ALIEN",
             "MEMENTO", "SHINIG", "GREATDITECTOR", "AMBULANCE", "TITANIK", "DIEHARD"]
Bollywood = ["RAAZ", "ROBOT", "SINGHAM", "MARD", "TOOFAN", "VIVAH", "SHERSHAH", "UDAAN", "BROTHERS", "PLAYERS", "RAEES",
             "DILWALE", "KAABIL", "OKJAANU", "SANJU", "SULTAN", "TANHAJI", "PADMAVAT", "KABIRSINGH", "SIMBBA",
             "SOORYANVANSHI", "KESARI", "CHHICHHORE", "DABBANGG", "DANGAL", "AIRLIFT", "BADHAIHO", "ROWDYRATHORE",
             "RRAJKUMAR"]
x = int(input("Enter 1 for Hollywood Movie and 2 for Bollywood Movie "))
initial_time = int(time.time())
if x == 1:
    a = (random.choice(Hollywood))
    c = []
    for v in range(len(a)):
        k = a[v]
        c.append(k)
    b = list("*" * len(a))
    print(b)
    for i in range(len(a) + 3):
        current_time = int(time.time()) - initial_time
        print(f"Time completed is {current_time} Seconds")
        x = input()
        for j in range(len(b)):
            if a[j] == x:
                b[j] = x
            else:
                None
        print(b)
    if b == c:
        print("Congrats!!!!!!!! you won the game......")
        m = "".join(b)
        print(f"The correct answer is {m}")
        quit()
    else:
        print(f"OOOPPPPSSSS!!!!!!! You Loose the game. The correct answer was {a}")
        quit()
if x == 2:
    a = (random.choice(Bollywood))
    c = []
    for v in range(len(a)):
        k = a[v]
        c.append(k)
    b = list("*" * len(a))
    print(b)
    for i in range(len(a) + 3):
        current_time = int(time.time()) - initial_time
        print(f"Time completed is {current_time} Seconds")
        x = input()
        for j in range(len(b)):
            if a[j] == x:
                b[j] = x
            else:
                continue
        print(b)
    if b == c:
        print("Congrats!!!!!!!! you won the game......")
        m = "".join(b)
        print(f"The correct answer is {m}")
        quit()
    else:
        print(f"OOOPPPPSSSS!!!!!!! You Loose the game. The correct answer was {a}")
        quit()
else:
    print("Thik se Enter Karo")