'''
# command + k + c = yorum satırı
# command + k + u = yorum satırı kaldır

x = input('1. sayı: ')
y = input('2. sayı: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)
print(toplam)
print(type(toplam))
print("x'in tipi => ", type(x))
'''
# print("sa")

r = input("yarı çap: ")
π = 3.14

r = float(r)

daireAlani = (π * (r ** 2))
daireCevresi = (2 * π * r)
yazdir = "Alan: " + str(daireAlani) + " | Çevre: " + str(daireCevresi)
karakterSayisi = len(yazdir)
print(yazdir[karakterSayisi - 1])



