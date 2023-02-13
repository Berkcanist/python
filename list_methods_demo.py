names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1
names.append('Cenk')

#2
names.insert(0, 'Sena')

#3
# del names[-2]
# names.remove('Deniz')
# print(names)

#4
result = names.index('Deniz')

#5
result = 'Ali' in names

#6
# names.reverse()

#7
names.sort()


#8
years.sort()

#9
cars = 'Chevrolet,Dacia'.split(',')
# print(cars)

#10
result = min(years)
result = max(years)

#11
result = years.count(1998)

#12
years.clear()

#13
markalar = []

marka1 = input("1. Marka :")
markalar.append(marka1)

marka2 = input("2. Marka :")
markalar.append(marka2)

marka3 = input("3. Marka :")
markalar.append(marka3)

print(markalar)

# print(names)
# print(years)
# print(result)
