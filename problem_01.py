#1. Write a program to store seven fruits in a list entered by the user?

fruits = []
 
f1 = input("Enter Fruit name : ")
fruits.append(f1)

f2 = input("Enter Fruit name : ")
fruits.append(f2)

f3 = input("Enter Fruit name : ")
fruits.append(f3)
f4 = input("Enter Fruit name : ")
fruits.append(f4)
f5 = input("Enter Fruit name : ")
fruits.append(f5)
f6 = input("Enter Fruit name : ")
fruits.append(f6)
f7 = input("Enter Fruit name : ")
fruits.append(f7)
print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
 
m1 =int(input("Enter marks  : "))
marks.append(m1)

m2 =int(input("Enter marks  : "))
marks.append(m2)

m3 =int(input("Enter marks  : "))
marks.append(m3)
m4 =int(input("Enter marks  : "))
marks.append(m4)
m5 =int(input("Enter marks  : "))
marks.append(m5)

m6 =int(input("Enter marks  : "))
marks.append(m6)

# to sort
marks.sort()

print(marks)

