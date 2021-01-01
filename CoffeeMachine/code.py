''' Kahve Makinasının çalışma mantığı ile yazılan bu kod, fonsiyon yapılarını
global - yerel değişkenleri ve while yapısı ile fonksiyonları iç içe kullanarak bir
sonuç elde etmek için faydalı bir pratiktir.

Çalışma Mantığı:
hazırlanan menü ile verilmiş olan içerik ve fiyatlar üzerinden kullanıcıya istediği kahve sorulmakta
ve bu kahve için ödeme yapması istenmektedir. 

Fiyatı ve ürünleri belli olan kahve ödemenin veya malzemelerin yetersiz gelmesi halinde kahveyi yapmamakta,
aksi durumda ise kahveyi hazrlamaktadır. 

Kahve hazırlandıktan sonra malzemelerden yapılan kahve için kullanılan kısım düşürülmekte, kullanıcının girdiği
ücretin kalanı kullanıcıya iade edilirken kahve fiyatı kadar olan kısmı kasaya eklenmektedir. '''



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 1- Kaynak Kontrol
def kaynak_kontrol(kahve):
    for i in kahve:
        if kahve[i] > resources[i]:
            print(f"yeterli {i} yok.")
            return False
    return True

drink = MENU["latte"]
kaynak_kontrol(drink["ingredients"])


# 2- Para Kontrol
def parakontrol():
    total= int(input("1 KURUŞ: ")) *0.01
    total+= int(input("10 KURUŞ: ")) *0.1
    total+= int(input("25 KURUŞ: ")) *0.25
    return total

# 3- Para iade
profit = 0
def odeme(girdi, fiyat):
    if girdi>= fiyat:
        kalan = round(girdi - fiyat,2)
        print(f"{kalan}, para üstünüz.")
        global profit
        profit+=fiyat
        return True
    else:
        print("girdiğiniz ücret yetersizdir.")
        return False

# 4- Kahve Yapımı
def makecoffee(secim, icerik):
    for i in icerik:
        resources[i] -= icerik[i]
    print(f"☕ {secim} hazır! afiyet olsun.")

# 5- While döngüsü ve Rapor döndürme
machine_on = True
while machine_on:
    secim = str(input("Hoş geldiniz! Kahve Seçiniz (latte-cappuccino-espresso) : "))
    if secim == "off":
        machine_on = False
    elif secim == "rapor":
        print(f"Kalan su: {resources['water']} ml")
        print(f"kalan süt: {resources['milk']} ml")
        print(f"kalan kahve: {resources['coffee']} gram")
        print(f"kasada {profit}$ var")
    else:
        kahve = MENU[secim]
        if kaynak_kontrol(kahve["ingredients"]):
            para = parakontrol()
            if odeme(para, kahve["cost"]):
                makecoffee(secim, kahve["ingredients"] )

