print("loading...")
from msilib.schema import Class
import sys
import time
def typed(string, t = 0.02, end = True):
    for i in string:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(t)
    if end:
        print()

money = 0

import os
import random
import secrets
import sys
clear = lambda: os.system('cls')
spacing = "    "
x = 0
y = 0

Tiles = {
    "ground": ["░","▒","▓"]
}

World = []

wxs = 40
wys = 20


for i in range(wys):
    World.append([])
    for v in range(wxs):
        World[i].append("X")

# World = [
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"],
#     ["X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X" , "X"]
# ]

for i in range(len(World)):
    for v in range(len(World[i])):
        World[i][v] = random.choice(Tiles["ground"])

Worlddat = [
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None],
    [None , None , None , None , None , None , None , None , None , None , None , None , None]
]

Map = []

for i in range(len(World)):
    Map.append([])
    for v in range(len(World[i])):
        Map[i].append("#")



EMAP = [
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
]

for i in range(100):
    World[secrets.randbelow(wys)][secrets.randbelow(wxs)] = "O"

playerg = "P"

def mapr():
    global playerg
    for i in range(len(Map)):
        string = ""
        for v in range(len(Map[i])):
            if i == y and v == x:
                string += playerg
            else:
                string += Map[i][v]
        print(spacing + string)
    playerg = "P"

UIPT = ""
running = True
secret = 0
secretnumbers = [
    4,
    8,
    12
]

eventslog = []

greetings = ["hello", "greetings"]

def printt(text):
    print("  " + text)

clear()
print("-------------------------------------------")
print(
"""
     START - START
     INFO - INFO
     CREDITS - CREDITS
     EXIT - EXIT

"""
)
while UIPT != " START ":
    UIPT = " " + input(spacing + "> ").upper() + " "
    if UIPT == " INFO ":
        0+0
    elif UIPT == " CREDITS ":
        0+0
    elif UIPT == " EXIT ":
        typed("exiting...")
        os.abort()
    elif UIPT == " START ":
        break
    else:
        typed(spacing + "Type one of the valid commands.")
clear()
Map[y][x] = World[y][x]

while running:
    playerg = "P"
    Map[y][x] = World[y][x]
    UIPT = " " + input(spacing + "> ").upper() + " "
    try:
        if UIPT == " MAP ":
            mapr()
        elif UIPT == " NORTH ":
            clear()
            if y > 0:
                y -= 1
                Map[y][x] = World[y][x]
                if World[y][x] == "O":
                    playerg = "R"
            mapr()
        elif UIPT == " SOUTH ":
            clear()
            if y < len(Map) - 1:
                y += 1
                Map[y][x] = World[y][x]
                if World[y][x] == "O":
                    playerg = "R"
            mapr()
        elif UIPT == " EAST ":
            clear()
            if x < len(Map[y]) - 1:
                x += 1
                Map[y][x] = World[y][x]
                if World[y][x] == "O":
                    playerg = "R"
            mapr()
        elif UIPT == " WEST ":
            clear()
            if x > 0:
                x -= 1
                Map[y][x] = World[y][x]
                if World[y][x] == "O":
                    playerg = "R"
            mapr()
        elif UIPT == " LOOK ":
            if World[y][x] == "O":
                clear()
                World[y][x] = random.choice(Tiles["ground"])
                money += 1
                playerg = "P"
                mapr()
                typed(spacing + "you found some constant!")
            elif World[y][x] == "A":
                typed(spacing + "just a normal house")
            else:
                typed(spacing + "nothing here")
        elif UIPT == " BUILD ":
            typed(spacing + "build a house here for 1 constant? ", 0.02, False)
            answer = input()
            if money < 1:
                typed(spacing + "sorry you can't avoid a house")
            elif answer == "y":
                typed(spacing + "house built!")
                World[y][x] = "A"
                money -= 1

            elif answer == "n":
                typed(spacing + "ok")
            else:
                typed(spacing + "answer not recognized")
            clear()
            mapr()
        elif UIPT == " CHAT ":
            if World[y][x] == "A":
                typed(spacing + "\"" + random.choice(greetings) + "\" you tell the residents" )
        elif UIPT == " MAPL ":
            Map = World
    except:
        None
    if World[y][x] == "O":
        playerg = "R"
    else:
        playerg = "P"