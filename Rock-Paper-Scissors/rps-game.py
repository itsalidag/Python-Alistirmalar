#rps gme

import random
import pandas as pd
secenek = ["Taş", "Kağıt", "Makas"]
kullanıcıskor = 0
robotskor = 0
a = 0
while a < 10:
    secim = random.randint(0,2)
    robotsecim = secenek[secim]
    kullanıcı = str(input("Taş için (T), Kağıt için (K), Makas için (M) kullan ----> "))
    if kullanıcı in ["T","t"]:
        if robotsecim == secenek[0]:
            continue
        elif robotsecim == secenek[1]:
            robotskor = robotskor+1
            print("Robot +1")
        elif robotsecim == secenek[2]:
            kullanıcıskor = kullanıcıskor+1
            print("İnsan +1")
    if kullanıcı in ["k","K"]:
        if robotsecim == secenek[0]:
            kullanıcıskor = kullanıcıskor +1
            print("İnsan +1")
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
            print("İnsan +1")
        elif robotsecim == secenek[2]:
            print("Aynıyız, sayılmaz")
            continue          
    print("Tur: {}".format(a))
    a = a+1

print("Oyun sonu! Kazanan {}, skor = robot : {} İnsan: {}".format(("robot" if robotskor>kullanıcıskor else "İnsan"), robotskor,kullanıcıskor))
