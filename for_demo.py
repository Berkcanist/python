sayilar = [1,3,5,7,9,12,19,21]

#1
# for uc in sayilar:
#     if uc % 3 == 0:
#         print(f"{uc} -> 3'ün katıdır")
#     else:
#         print(f"{uc} -> 3'ün katı değildir")


#2
# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

#3
# for sayi in sayilar:
#     if sayi % 2 == 1:
#         sayi = sayi**2
#         print(sayi)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize', 'ağrı', 'kesici']

#4
# for x in sehirler:
#     i = 0
#     for y in x:
#         i = i + 1
#     if i <= 6:
#         print(x)
#################################
# for sehir in sehirler:
#     if (len(sehir) <= 5):
#         print(sehir)


urunler = [
    {'name':'samsung S5', 'price': '3000'},
    {'name':'samsung S6', 'price': '4000'},
    {'name':'samsung S7', 'price': '5000'},
    {'name':'samsung S8', 'price': '6000'},
    {'name':'samsung S9', 'price': '7000'}
]

#5
# toplam = 0
# for telefon in urunler:
#     #print(telefon['price'])
#     toplam += int(telefon['price'])
# print(toplam)

#6
for telefon in urunler:
    if int(telefon['price']) <= 5000:
        print(telefon['name'])