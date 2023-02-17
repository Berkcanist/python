sayilar = [1,3,5,7,9,12,19,21]

#1
# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1

#2
# start = int(input('Başlangıç değerini giriniz: '))
# end = int(input('Bitiş değerini giriniz: '))
# x = start
# while x < end:
#     x += 1
#     if x % 2 == 1:
#         print(f'"{x}" sayısı {start} ve {end} arasındaki sayılarda bulunan tek sayıdır!')

#3
# sayi = 100

# while sayi-1 > 1:
#     sayi -= 1
#     print(sayi)

#4
# i = 0
# numbers = {}
# while i < 5:
#     numbers[i] = int(input(f'{i+1}. Sayıyı Giriniz: '))
#     i += 1
# i = 0
# while i < 5:
#     print(numbers[i])
#     i += 1

#5
urunSayisi = int(input('Ürün sayısını giriniz: '))
urunler = []

while urunSayisi > 0:
    name = input('Ürün ismi: ')
    price = input('Ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    urunSayisi -= 1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ------- ürün fiyatı: {urun['price']}")