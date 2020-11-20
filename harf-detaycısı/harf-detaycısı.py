import random

name = str(input("İncelenecek isim: "))

def split(string):
    return [char for char in string]

harfler = split(name)
sesliler = []
sessizler = []
for harf in harfler:
    if harf in ("a","e","ı","i","o","ö","u","ü"):
        sesliler.append(harf)
    elif harf in ("b","c","ç","d","f","g","ğ","h","j","k","l","m","n","p","r","s","ş","t","v","y","z"):
        sessizler.append(harf)

print("Kelimede sesli harf sayısı = "+ str(len(sesliler)))
print("Kelimede sessiz harf sayısı = "+str(len(sessizler)))
print("Kelimede Sessiz Harfler = "+str(sessizler))
print("Kelimede Sesli Harfler = "+str(sesliler))

distinct_sesli = "".join(set(sesliler))
distinct_sessiz = "".join(set(sessizler))

print("Kelimenin özü = "+ str(distinct_sesli)+str(distinct_sessiz))
print("Bu kelimede {} farklı harf kullanılmış.".format(len(distinct_sesli)+len(distinct_sessiz)))