import random
import datetime
import io
import math
def print_hand(za_hando):
        matrixLength = len(za_hando)
        matrix = []
        for i in range(math.floor(matrixLength/4) + 1):
                for j in range(7):
                        matrixRow = []
                        for k in range(4):
                                matrixRow.append("           ")
                        matrix.append(matrixRow)
        for i in range(len(za_hando)):
                column=i%4
                row=(math.floor(i/4))*7-1
                for j in range(7):
                        row +=1
                        matrix[row][column] = ascii_art[default_deck.index(za_hando[i])]
        for i in matrix:
                print(''.join(i))
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
