## Lifetime seconds  counter


from datetime import *

datem = datetime.today()
user = str(input("Doğum tarihinizi gün-ay-yıl formatında giriniz : "))
splitted = user.split("-")
userdate = date(int(splitted[2]), int(splitted[1]), int(splitted[0]))
tanısma = str(input("ikinci tarih: "))
nitelik = input("Günün niteliği: ")
ikincispl = tanısma.split("-")
ikincill = date(int(ikincispl[2]), int(ikincispl[1]), int(ikincispl[0]))
today = date(datem.year, datem.month, datem.day)
delta = today - userdate
ikincitarihle = today - ikincill
birliktegecenoran = (ikincitarihle * 100) / delta
roundladım = round(birliktegecenoran, 2)
print(str(user) + "'den beri " + str(delta.days) + " gün geçmiş... Maşallah.")
print(str(tanısma) + " dan beri " +str(nitelik)+ " ile " + str(ikincitarihle.days)+ " gündür birliktesin.")
print(str(nitelik) + ", hayatının %"+ str(roundladım) + " lik kısmında seninle birlikteydi. Allah arttırsın.")
