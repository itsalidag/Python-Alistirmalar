#rps gme

import random
import pandas as pd
secenek = ["Taş", "Kağıt", "Makas"]
kullanıcıskor = 0
robotskor = 0
a = 0
oyuncuadi = str(input("Oyuncu Adı: "))
while a < 10:
    secim = random.randint(0,2)
    robotsecim = secenek[secim]
    kullanıcı = str(input("Taş için (T), Kağıt için (K), Makas için (M) kullan ----> "))
    if kullanıcı in ["T","t"]:
        if robotsecim == secenek[0]:
            print("Aynıyız, sayılmaz.")
            continue
        elif robotsecim == secenek[1]:
            robotskor = robotskor+1
            print("Robot +1")
        elif robotsecim == secenek[2]:
            kullanıcıskor = kullanıcıskor+1
            print("{} +1".format(oyuncuadi))
    if kullanıcı in ["k","K"]:
        if robotsecim == secenek[0]:
            kullanıcıskor = kullanıcıskor +1
            print("{} +1".format(oyuncuadi))
        elif robotsecim == secenek[1]:
            print("Aynıyız, sayılmaz")
            continue   
        elif robotsecim == secenek[2]:
            robotskor = robotskor+1
            print("Robot +1")
    if kullanıcı in ["m","M"]:
        if robotsecim == secenek[0]:
            robotskor = robotskor +1
            print("Robot +1")
        elif robotsecim == secenek[1]:
            kullanıcıskor = kullanıcıskor+1
            print("{} +1".format(oyuncuadi))
        elif robotsecim == secenek[2]:
            print("Aynıyız, sayılmaz")
            continue          
    print("Tur: {}".format(a))
    a = a+1

print("Oyun sonu! Kazanan {}, skor = robot : {} {}: {}".format(("robot" if robotskor>kullanıcıskor else oyuncuadi), robotskor,oyuncuadi,kullanıcıskor))

