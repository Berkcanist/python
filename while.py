#1-100 e kadar

# x = 0

# while x <= 100:
#     print(x)
#     x += 1

name = '' # Falsa
while not name.strip():
    name = input('İsminizi giriniz: ')
print(f'Merhaba, {name}!')