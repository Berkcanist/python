website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"


#1
result = ' Hello World '
# print(result.strip())

#2
result = website.replace("http://www.sadikturan.com", "sadikturan")
result = 'wwwa.sadikturan.com'.strip('w.moca')

#3
result = course.lower()

#4
result = website.count('a')

#5

result = website.startswith('www')
result = website.endswith('com')

#6

result = website.find('.com')

#7

result = course.isalpha()


#8

a = 'Contents'
result = a.center(50,'*')

#9

result = course.replace(' ', '-')


#10

result = "Hello World".replace('World', 'There')

#11

result = course.split()
result = result[2][1]

print(result)

