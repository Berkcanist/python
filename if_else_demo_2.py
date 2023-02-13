#1
# sayi = float(input('Sayı: '))
# if 0 < sayi < 100:
# 	print('Sayı 0 ile 100 arasındadır!')
# else:
# 	print('Sayı 0 ile 100 arasında değildir!')

#2
# sayi = int(input('Sayı: '))
# if sayi > 0 and sayi % 2 == 0:
#    print('Sayı hem pozitif hem de çift sayıdır.')
# elif sayi > 0:
#       print('Sayı pozitiftir ama çift değildir.')
# elif sayi % 2 == 0:
#    print('Sayı çifttir ama pozitif değildir.')
# else:
#    print('Sayı pozitif de değildir çift de değildir.')     

#3
# email = 'berkcan.0942@gmail.com'
# passwd = 'Berkcan.09'

# girilenEmail = input('email: ')
# girilenPasswd = input('password: ')

# if email == girilenEmail:
#    if passwd == girilenPasswd:
#       print('Giriş başarılı!')
#    else:
#       print('Girmiş olduğunuz parola yanlıştır!')
# else:
#    print('Girmiş olduğunuz email yanlıştır!')

#4
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# max = a
# if max < b:
#    max = b
# if max < c:
#    max = c

# print('En büyük sayı',max)

#5
# vize1 = int(input('1. Vize: '))
# vize2 = int(input('2. Vize: '))
# final = int(input('Final: '))

# ortalama = ((vize1 + vize2) / 2) * 0.6 + (final * 0.4)

# if final < 70:
#    if ortalama >= 50 and final >= 50:
#       print('Geçti')
#    else:
#       print('Kaldı')
# else:
#    print('Geçti')

#6
# hg = float(input('Boy: '))
# kg = float(input('Kilo: '))

# endeks = kg / (hg**2)
# if 0 <= endeks <= 18.4:
#    print('Zayıf')
# if 18.4 < endeks <= 24.9:
#    print('Normal')
# if 24.9 < endeks <= 29.9:
#    print('Kilolu')
# if 29.9 < endeks <= 34.9:
#    print('Obez')
# print('Endeks: ',endeks)