#1
cars = ['Bmw','Mercedes','Opel','Mazda']

#2
len  = len(cars)

#3
result = cars[0]
result = cars[len - 1]

#4
# cars[len - 1] = 'Toyota'
result = cars

#5
result = cars.count('Mercedes')
result = 'Mercedes' in cars

#6
result = cars[-2]

#7
result = cars[:3]

#8
cars[-2:] = ['Toyota', 'Renault']
deneme = cars
# print(deneme)
#9
result = cars + ['Audi','Nissan']
# cars.append('Audi')
# cars.append('Nissan')
# result = cars
#10
del cars[-1]
result = cars
# cars.remove('Nissan')

#11
result = cars[::-1]

#12

studentA = ['Yiğit','Bilgi',2010, [70, 60, 70]]
studentB = ['Sena','Turan',1999, [80, 80, 70]]
studentC = ['Ahmet','Turann',1998, [80, 70, 90]]

result = [studentA, studentB, studentC]

print(result[2][3][0])

