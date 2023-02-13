#key - value

# 41 => Kocaeli      34 => İstanbul

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [41, 34]

# print(plakalar[sehirler.index('Kocaeli')])

#olmasını istediğim
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

plakalar = { 'Kocaeli' : 41, 'İstanbul' : 34}

# print(plakalar['İstanbul'])

plakalar['Aydın'] = 9
plakalar['Kocaeli'] = 'new value'

# print(plakalar)



users = {
	1 :{
		'name': 'Berkcan',
		'age': 20,
		'roles': ['admin', 'user'],
		'mail': 'berkcan@gmail.com',
		'phone': 5412444756
	},
	2 :{
		'name': 'Ahmet',
		'age': 18,
		'roles': ['user'],
		'mail': 'ahmet@gmail.com',
		'phone': 5313223586
	},
	3 :{
		'name': 'Abdürrezzak',
		'age': 31,
		'roles': ['otuzbirci'],
		'mail': 'abdürrezzak@gmail.com',
		'phone': 5313313131
	}
}
# print(users[3]['roles'])
print(users[1]['roles'][0])

