number = input('Öğrenci No: ')
ad = input('Adı: ')
soyad = input('Soyadı: ')
telefon = input('Telefonu: ')



students = {}

#students['1.ögrenci'] = {'ad': ad, 'soyad': soyad, 'telefon': telefon, 'ogrenci numarası': input('Ogrenci Numarası: ')}
students[number] = {'ad': ad, 'soyad': soyad, 'telefon': telefon}

number = input('Öğrenci No: ')
ad = input('Adı: ')
soyad = input('Soyadı: ')
telefon = input('Telefonu: ')

number1 = input('Öğrenci No: ')
ad1 = input('Adı: ')
soyad1 = input('Soyadı: ')
telefon1 = input('Telefonu: ')

#students['2.ögrenci'] = {'ad': ad, 'soyad': soyad, 'telefon': telefon, 'ogrenci numarası': input('Ogrenci Numarası: ')}
#students[number] = {'ad': ad, 'soyad': soyad, 'telefon': telefon}

students.update({
	number: {
		'ad': ad,
		'soyad': soyad,
		'telefon': telefon
	},
	number1: {
		'ad': ad1,
		'soyad': soyad1,
		'telefon': telefon1
	}
})

#print(students['1158']['ad'])
print(students)

ogrenciNumarasi = input('İstediğiniz öğrencinin numarasını giriniz: ')
print(students[ogrenciNumarasi])
