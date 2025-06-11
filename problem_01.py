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

# 3. Check that a tuple type cannot be changed in python.
 
touple1 = ( 'hii', 121,"true")

#touple1[1]=128
# TypeError: 'tuple' object does not support item assignment

print(touple1)

# Write a program to sum a list with 4 numbers.

list=[3,5,6,1]
print(sum(list))

# Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
n=a.count(0)
print(n)


# chapter 5 - dictonary 
a={
    "name": "harry",
"from": "india",
"marks": [92,98,96]
}
print(a.items())

print(a.keys())

print(a.values())

# dict_items([('name', 'harry'), ('from', 'india'), ('marks', [92, 98, 96])])
# dict_keys(['name', 'from', 'marks'])
# dict_values(['harry', 'india', [92, 98, 96]])

a.update({"Percent": "96%",'marks' :[90,98,96]})
print(a)

# sets

# practice set 5
 
 
# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 