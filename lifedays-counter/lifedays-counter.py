## Lifetime seconds  counter


from datetime import *

datem = datetime.today()
user = str(input("Doğum tarihinizi gün-ay-yıl formatında giriniz : "))
splitted = user.split("-")
userdate = date(int(splitted[2]), int(splitted[1]), int(splitted[0]))

today = date(datem.year, datem.month, datem.day)
delta = today - userdate
print("Bugüne dek," + str(delta.days) + "gün geçmiş... Maşallah.")