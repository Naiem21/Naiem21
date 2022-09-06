#Q1
# def printValue(num):
#     if num == '1':
#         print("One",end=" ")
#     elif num== '2':
#         print("Two",end=" ")
#     elif num== '3':
#         print("Three",end=" ")
#     elif num== '4':
#         print("Four",end=" ")
#     elif num== '5':
#         print("Five",end=" ")    

# def printWord(N):
#     i = 0
#     length = len(N)
#     while i < length:       
#         printValue(N[i])
#         i += 1
# N = input("Enter the number of digits : ")
# printWord(N)

#Q2
# number = int(input("Number Enter the number : "))
# if number % 2 == 0:
#     print("Number is even ")
# else:
#     print("Number is odd ")

#Q3
# ch = input("Enter the character : ")
# if (ch =='a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u' or 
#     ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#     print("Character is vowel")
# else:
#     print("Character is not vowel")

##Q4
# Day=int(input("Enter the day 1-7 : "))
# if (Day == 1):
#     print(Day,"is Sunday")
# elif (Day == 2):
#     print(Day,"is Monday")
# elif (Day == 3):
#     print(Day,"is Tuesday")
# elif (Day == 4):
#     print(Day,"is Wednesday")
# elif (Day == 5):
#     print(Day,"is Thursday")
# elif (Day == 6):
#     print(Day,"is Friday")
# elif (Day == 7):
#     print(Day,"is Saturday")

#Q5
# Month =int(input("Enter the month 1-12 : "))
# if (Month == 1):
#     print(Month,"is January")
# elif (Month == 2):
#     print(Month,"is February")
# elif (Month == 3):
#     print(Month,"is March")
# elif (Month == 4):
#     print(Month,"is April")
# elif (Month == 5):
#     print(Month,"is May")
# elif (Month == 6):
#     print(Month,"is June")
# elif (Month == 7):
#     print(Month,"is July")
# elif (Month == 8):
#     print(Month,"is August")
# elif (Month == 9):
#     print(Month,"is September")
# elif (Month == 10):
#     print(Month,"is October")
# elif (Month == 11):
#     print(Month,"is November")
# elif (Month == 12):
#     print(Month,"is December")

#Q6

# choice = int(input("Enter the choice : "))
# print("Enter the 2 number :")
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# if (choice == 1):
#     Add=num1+num2
#     print(Add)
# elif (choice == 2):
#     Sub=num1-num2
#     print(Sub)
# elif (choice == 3):
#     Mul=num1*num2
#     print(Mul)
# elif (choice == 4):
#     Div=num1/num2
#     print(Div)
# else:
#     print("Unknown choice")

#Q7

# x=int(input("Enter the value of X :"))
# y=int(input("Enter the value of Y :"))
# if x>y:
#     print("X is greater then Y")
# else:
#     print("Y is greater then X")

#Q8

# number = int(input("Enter the number : "))
# if number == 0 :
#     print("Number is zero")
# elif number > 0:
#     print("Number is positive")
# else:
#     print("Number is negative")

#Q9
# number = int(input("Enter the number : "))
# if (number % 3 == 0 ) & (number % 4 == 0) & (number % 8 == 0) :
#     print("Number is divisible ")
# else:
#     print("Number is not divisible")

#Q10
# number = int(input("Enter the number : "))
# if number in range(100,200):
#     print("Number is in range 100-200")
# else:
#     print("Number is not in range 100-200")

#Q11

# x=int(input("Enter the value of X :"))
# y=int(input("Enter the value of Y :"))
# z=int(input("Enter the value of Z :"))
# if x>y and x>z:
#     print("X is greater then Y and Z")
# elif y>z:
#     print("Y is greater then X and Z")
# else:
#     print("Z is greater then X and Y")


#Q12

# marks=int(input("Enter the marks : "))
# if marks >100:
#     print("not in marks") 
# elif marks >= 75 :
#     print("A")
# elif marks >= 60:
#     print("B") 
# elif marks >= 50:
#     print("C") 
# elif marks >= 40:
#     print("D") 
# elif marks < 40:
#     print("Fail")

#Q14

# year =int(input("Enter the year : ")) 
# if(year % 4 == 0) and(year % 100 != 0):
#     print("This is leap year")
# elif(year % 400 == 0) and (year % 100 != 0):
#     print("This is leap year")
# else:
#     print("This is not leap year")

#Q15

# rate = int(input('Enter price of product: '))
# quantity = int(input('Enter quantity: '))
# amount = rate * quantity

# if amount <= 2000:
#     discount = amount*0.04
# elif amount <= 7000:
#     discount = amount*0.08
# elif amount >= 7001:
#     discount = amount*0.10
# else:
#     discount = 0

# net_amount = amount - discount

# print('Total price:',amount)
# print('Discount amount:',discount)
# print('Your net amount is',net_amount)

#Q16

# held=int(input("Enter the classes held count: "))
# att=int(input("Enter the classes attended count: "))
# percentage=att/held*100
# if percentage > 75: 
#     print("Student allow to sit in exam ")
# else:
#     print("Student not allow to sit in exam ")

# print(" Student total percentage:",percentage)

#Q17

# Age=int(input("Enter the age: "))
# Gender=input("Enter the gender: ")
# Merital=input("Enter the merital:")

# if Gender =='F':
#     print("You will work only in urban areas")
# elif Gender =='M'and (Age >=20 and Age < 40):
#     print(" You will work anywhere ")
# elif Gender =='M' and (Age >=40 and Age < 60):
#     print(" You will work only in urban areas")
# elif not(Age < 20 and Age > 60):
#     print("ERROR")
    