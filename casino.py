import random
import datetime
import io
import math
def print_card(ajdi):
    if ajdi.startswith("9"):
        if ajdi.endswith("♥"):   #Yandere dev ahhhhhh
            for i in range(7):
                print(ascii_art[0][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[1][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[2][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[3][i])
    elif ajdi.startswith("10"):
        if ajdi.endswith("♥"):
            for i in range(7):
                print(ascii_art[4][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[5][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[6][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[7][i])
    elif ajdi.startswith("J"):
        if ajdi.endswith("♥"):
            for i in range(7):
                print(ascii_art[8][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[9][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[10][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[11][i])
    elif ajdi.startswith("Q"):
        if ajdi.endswith("♥"):
            for i in range(7):
                print(ascii_art[12][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[13][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[14][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[15][i])
    elif ajdi.startswith("K"):
        if ajdi.endswith("♥"):
            for i in range(7):
                print(ascii_art[16][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[17][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[18][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[19][i])
    elif ajdi.startswith("A"):
        if ajdi.endswith("♥"):
            for i in range(7):
                print(ascii_art[20][i])
        elif ajdi.endswith("♦"):
            for i in range(7):
                print(ascii_art[21][i])
        elif ajdi.endswith("♣"):
            for i in range(7):
                print(ascii_art[22][i])
        elif ajdi.endswith("♠"):
            for i in range(7):
                print(ascii_art[23][i])
def print_hand(za_hando):
    for i in range(7):
        for j in range(math.ceil(len(za_hando)/2)):
                if za_hando[j].startswith("9"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[0][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[1][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[2][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[3][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("10"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[4][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[5][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[6][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[7][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("J"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[8][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[9][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[10][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[11][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("Q"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[12][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[13][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                        
                            print(ascii_art[14][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[15][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("K"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[16][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[17][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[18][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[19][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("A"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[20][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[21][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[22][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[23][i].rstrip("\n"), end="")
        print("")
    for i in range(7):
        for j in range(math.ceil(len(za_hando)/2),len(za_hando)):
                if za_hando[j].startswith("9"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[0][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[1][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[2][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[3][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("10"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[4][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[5][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[6][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[7][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("J"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[8][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[9][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[10][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[11][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("Q"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[12][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[13][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                        
                            print(ascii_art[14][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[15][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("K"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[16][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[17][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[18][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[19][i].rstrip("\n"), end="")
                elif za_hando[j].startswith("A"):
                    if za_hando[j].endswith("♥"):
                            print(ascii_art[20][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♦"):
                            print(ascii_art[21][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♣"):
                            print(ascii_art[22][i].rstrip("\n"), end="")
                    elif za_hando[j].endswith("♠"):
                            print(ascii_art[23][i].rstrip("\n"), end="")
        print("")
dt = datetime.datetime.now()
seed=dt.day*dt.month + (dt.second+15)*random.randint(7,15)*(dt.hour+16)*(dt.minute+67) + (dt.hour+18)*(dt.minute+23)*random.randint(43,56) + (dt.hour+5)*random.randint(967,1147) + (dt.second+3)*(dt.minute+9)*random.randint(87,114) + (dt.second+7)*(dt.hour+4)*random.randint(13,21)+dt.year*dt.month*dt.day*(dt.hour + 1)*(dt.minute+1)*(dt.second+1)*random.randint(1,10)
random.seed()
print(seed)
file = io.open("ascii.txt",mode="r",encoding="utf-8")
global ascii_art
ascii_art = []
for i in range(24):
    ascii_art.append([])
    for j in range(7):
        ascii_art[i].append(file.readline().rstrip("\n"))
default_deck = ["9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠","A♥","A♦","A♣","A♠"]
deck = ["9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠","A♥","A♦","A♣","A♠"]
random.shuffle(deck)
hand = []
hand = deck[0:7]
del deck[0:7]
print(' '.join(hand))
print_hand(hand)
