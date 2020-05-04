## Task 1.2 - Numbers divisible by 7 and not by 5

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        new.append(i)
print(new)

## Task 1.3 - User input and reverse

First_Name = input("Enter first Name: ")
Last_Name = input("Enter last Name: ")

print(First_Name[::-1] + " " + Last_Name[::-1])

## Task 1.4 - Sphere volume

D = 12
pi = 3.142
Sphere_formula = 4/3*pi*((D/2)**3)

print("the volume of the sphere is ",Sphere_formula)

## Task 2.1 - Sequence list for consecutive numbers

List = []
Lower = int(input("Enter the lower range: "))
Upper = int(input("Enter the upper range: "))

for i in range (Lower,Upper+1):
    List.append(i)
print(List)

## Task 2.2 - Pattern using nested loop

rows = int(input("enter the number of rows: "))

for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end=" ")
    print("\r")

for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*", end=" ")
    print("\r")

## Task 2.3 - Reverse User input

User_input = input("enter the input: ")

print("The reverse order of the user input is ", User_input[::-1])

## Task 2.4 - Sample output
Sample_output = ("WE, THE PEOPLE OF INDIA,\n   having solemnly resolved to constitute of India into a SOVEREIGN" +'!'+
"\n     SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n   and to secure to all its citizens")
print(Sample_output)









