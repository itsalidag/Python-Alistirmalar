

class mathali():
    def __init__(self):
        print("MathAli'ye Hoş geldin. İşte Yapabileceklerin")
        print("dalan() -> dikdörtgenin alanı")
        print("yalan() -> yamuk'un alanı")
        print("palan() -> paralelkenarın alanı")
        print("khac() -> küpün hacmi")

    def dalan(self,x,y):
        return x*y
    def yalan(self,alt_taban,ust_taban,yukseklik):
        return (alt_taban+ust_taban)*yukseklik/2
    def palan(self, taban, tabana_yukseklik):
        return taban*tabana_yukseklik
    def khac(self,kenar):
        return kenar*kenar*kenar
    def yuzde(self, x,y):
        # x, y nin yüzde kaçıdır? 
        return x*100/y
    def faiz(self, anapara, faiz_yuzde, zaman):
        return {"yıllık":(anapara*faiz_yuzde*zaman/100), "aylık" : (anapara*faiz_yuzde*zaman/1200), "gunluk":(anapara*faiz_yuzde*zaman/3600)}
    



math = mathali()
print(math.faiz(25000,1.2,750))