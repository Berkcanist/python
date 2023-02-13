values = 1, 2, 3

x, y, z = values    # fazla veya eksik değer varsa bize hata döndürecektir


values = 1, 2, 3, 4, 5

x, y, *z = values

print(x,y,z)
print(x,y,z[2])
