#1

# age = int(input('Yaş: '))

# if (age >= 18):
# 	school = input('Okul: ')
# 	if (school == 'üniversite') or (school == 'lise'):
# 		print('Ehliyet alabilir!')
# 	else:
# 		print('Ehliyet alamaz! Çünkü en az lise mezunu olması gerekir.')
# else:
# 	print('Ehliyet alamaz! Çünkü 18 yaşından küçük.')

#2
# puan1 = int(input('1. Sınavdan aldığı not: '))
# puan2 = int(input('2. Sınavdan aldığı not: '))
# sozlu = int(input('Sözlüden aldığı not: '))

# ort = (puan1 + puan2 + sozlu) / 3

# if 0 <= ort <= 100:
# 	if (0 <= ort <= 24):
# 		result = 0
# 	elif (25 <= ort <= 44):
# 		result = 1
# 	elif (45 <= ort <= 54):
# 		result = 2
# 	elif (55 <= ort <= 69):
# 		result = 3
# 	elif (70 <= ort <= 85):
# 		result = 4
# 	elif (86 <= ort <= 100):
# 		result = 5
# 	print(f'Ortalaması {ort} ve değeri {result}')
# else:
# 	print('Geçersiz bir not girdiniz!')

#3
import datetime
now = datetime.datetime.today()
t = input('Aracın trafiğe çıkış tarihini "gün.ay.yıl" şekilde yazınız: ')
day, month, year = t.split('.')
aracTarihi = datetime.datetime(int(year), int(month), int(day))
fark = now - aracTarihi

if 0 <= fark.days <= 365:
	print(f'{fark.days} Gün olmuş, 1. Bakım')
elif 365 < fark.days <= 365*2:
	print(f'{fark.days} Gün olmuş, 2. Bakım')
elif 365*2 < fark.days <= 365*3:
	print(f'{fark.days} Gün olmuş, 3. Bakım')
else:
	print(f"{fark.days} Gün olmuş yuh aq. Senin araba Allah'a emanet knk :)")
