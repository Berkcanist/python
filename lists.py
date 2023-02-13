userA = ['Berkcan', 20]
userB = ['Sadık', 32]

users = [userA, userB]

# print(users[1][0])

numbers = [1,10,3,8,5,0,1]
letters = ['b','i','l','g','i','s','a','y','a','r']


numbers.append(20)
numbers.insert(3,31)
numbers.insert(-1,69)
# numbers.pop(0)
# numbers.pop(-1)
# numbers.pop()
# numbers.remove(31)

numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()

print(letters)
# print(len(letters))
print(letters.count('a'))

print(numbers)
# print(len(numbers))
print(numbers.count(1))

