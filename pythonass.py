# #square
# n=int(input("Enter the num :"))
# square=n*n
# print(square)

# sawp
# x=int(input("Enter the value of x :"))
# y=int(input("Enter the value of y :"))
# temp=x
# x=y
# y=temp
# print('the veluer of x after swapping: {}'.format(x))
# print('the veluer of y after swapping: {}'.format(y))

# without
# x=int(input("Enter the value of x :"))
# y=int(input("Enter the value of y :"))
# print("Before swapping :")
# print("The value of x : ",x,"and y : ",y)
# x,y=y,x
# print("After sawpping : ")
# print("value of x : ",x,"and y : ",y)

# triangle
# a=int(input("Enter the 1st side"))
# b=int(input("Enter the 2nd side"))
# c=int(input("Enter the 3rd side"))
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
# print("Aera of triangle=%.2f " %area)

# circle
# PI=3.14
# r=float(input("Enter the radius of circle : "))
# area=PI*r*r
# print("Aera of circle=%.2f " %area)

# simpleInterest
# p=float(input("Enter the principle :"))
# t=float(input("Enter the time : "))
# r=float(input("Enter the reat : "))
# Simple_interest=(p*t*r)/100
# print("Simple Interest is :",Simple_interest)

# kmtomm
# n=int(input("Enter the value in km :"))
# MM=n*10000000
# print('%0.2f kilometers is equal to %0.2f milimeters' %(n,MM))

# sumofthr
# num1 = int(input("Please Enter the First Number  = "))
# num2 = int(input("Please Enter the Second number = "))
# num3 = int(input("Please Enter the Third number  = "))
# sumOfThree = num1 + num2 + num3
# avgOfThree = sumOfThree / 3
# print('The sum of {0}, {1} and {2} = {3}'.format(num1,num2, num3, sumOfThree))
# print('The Average of {0}, {1} and {2} = {3}'.format(num1,num2, num3, avgOfThree))

# celsius
# C = int(input("Enter temperature in celsius: "))
# F = (C * 9/5) + 32
# print('%.2f Celsius is: %0.2f Fahrenheit' %(C, F))

# fahrenheit
# F = int(input("Enter temperature in Fahrenheit: "))
# C = (F -32) * 5/9
# print('%.2f Fahrenheit is: %.2f Celsius' %(F, C))

#squarefirstlast

# number = int(input("Enter the number : "))
# number = str(number)
# first_digit = int(number[0])
# last_digit = int(number[-1])
# sum= first_digit + last_digit
# print('sum of first and last digit of the number is',sum)

#a cashier

# def countCurrency(amount):
	
# 	notes = [2000, 1000, 500, 100,
# 			50, 20, 10, 5, 1]
				
# 	noteCounter = [0, 0, 0, 0, 0,
# 					0, 0, 0, 0]
	
# 	print ("Currency Count -> ")
	
# 	for i, j in zip(notes, noteCounter):
# 		if amount >= i:
# 			j = amount // i
# 			amount = amount - j * i
# 			print (i ," : ", j)

# # Driver code
# amount = 4526
# countCurrency(amount)


#print=int(input("enter the five subjects :"))

# Subject_1=float(input("Enter the marks :"))
# Subject_2=float(input("Enter the marks :"))
# Subject_3=float(input("Enter the marks :"))
# Subject_4=float(input("Enter the marks :"))
# Subject_5=float(input("Enter the marks :"))

# total , percentage= None , None

# total= Subject_1+Subject_2+Subject_3+Subject_4+Subject_5
# percentage=(total / 500.0)*100

# print("the Total is :", total,"/ 500.0")
# print(" the Percentages is", percentage,"%")

#  ASCII representation

# char=input("Please enter a character :")
# print("The ASCII value of "+ char + " is",ord(char)) 

# number=input("Enter the number : ")
# reverse=number[::-1]
# print(reverse)
# def sum(reverse):
#     sum=0
#     for i in range(reverse):
#         sum+=reverse
#     return sum
# print(sum(reverse))   

# num=int(input("Please enter number : "))
# Convert=chr(num)
# print(Convert)


# basic_salary=float(input("Please enter salary : "))
# TA=float(basic_salary*0.10)
# PF=float(basic_salary*0.078)
# DA=float(basic_salary*0.500)
# GS=float(basic_salary+DA+TA)
# NS=float(GS-PF)
# print(" GROSS SALARY  : ",GS)
# print(" NET SALARY  : ",NS)



# number=int(input("Enter the number : "))
# if number==0:
#     print("Number is zero")
# elif number<0:
#     print("Number is negative")
# else:
#     print("Number is positive")


# Number=input("Please enter three digits number : ")
# if (Number==Number[::-1]):
#     print("Number is palindrome ")
# else:
#     print("Number is not palindrome")


# number=int(input("Entetr the therr digits of number : "))
# temp=number
# sum=0
# while temp!=0:
#     k=temp%10
#     sum+=k*k*k
#     temp=temp//10
# if sum==number:
#     print ("Number is armstrong : ")
# else:
#     print("Number is not armstrong : ")    
    
    
# x=int(input("Enter the value of the x :"))
# y=int(input("Enter the value of the y :"))
# z=int(input("Enter the value of the z :"))
# if x>y and x>z:
#     print("x is greater")
# elif y>x and y>z:
#     print("y is greater")
# else:
#     print("z is greater")


# year = int (input("Enter the year : "))


# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# else:
#     print("{0} is not a leap year".format(year))


# ch=input("Enter the character :")
# if (ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'
#    or ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#     print("character is vowel !!!")
# else:
#     print("character is consonant !!!")    
    
    
# char=input("Enter the character : ")
# if char.isupper():
#     print("character is upper")
# elif char.islower():
#     print("character is lower")
# else:
#     print("not a character ")


# a = int(input('Enter first number  : '))
# b = int(input('Enter second number : '))
# c = int(input('Enter third number  : '))

# smallest = 0

# if a < b and a < c :
#     smallest = a
# elif b < c :
#     smallest = b
# else :
#     smallest = c

# print(smallest, "is the smallest of three numbers.")

# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# smallest=0
# if num1<num2 or num1<num3:
#     smallest=num1
# elif num2<num3 :
#     smallest=num2
# else:
#     smallest=num3
# print(smallest,"is smallest of three numbers ")


# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# smallest=0
# if num1<num2 or num1<num3:
#     smallest=num1
# elif num2<num3 :
#     smallest=num2
# else:
#     smallest=num3
# print(smallest,"is smallest of three numbers ")


# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# smallest=0
# if num1<num2 or num1<num3:
#     smallest=num1
# elif num2<num3 :
#     smallest=num2
# else:
#     smallest=num3
# print(smallest,"is smallest of three numbers ")


# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# smallest=0
# if num1<num2 or num1<num3:
#     smallest=num1
# elif num2<num3 :
#     smallest=num2
# else:
#     smallest=num3
# print(smallest,"is smallest of three numbers ")


# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# smallest=0
# if num1<num2 or num1<num3:
#     smallest=num1
# elif num2<num3 :
#     smallest=num2
# else:
#     smallest=num3
# print(smallest,"is smallest of three numbers ")


# num1= int(input("Enter the 1st number :"))
# num2= int(input("Enter the 2nd number :"))
# num3= int(input("Enter the 3rd number :"))
# largest=0
# if num1>num2 and num1>num3:
#     largest=num1
# elif num2>num3 and num2>num1:
#     largest=num2
# else:
#     largest=num3
# print(largest,"is largest of three numbers ")



# Subject_1=float(input("Enter the marks :"))
# Subject_2=float(input("Enter the marks :"))
# Subject_3=float(input("Enter the marks :"))
# Subject_4=float(input("Enter the marks :"))
# Subject_5=float(input("Enter the marks :"))

# total , percentage= None , None

# total= Subject_1+Subject_2+Subject_3+Subject_4+Subject_5
# percentage=(total / 500.0)*100

# print("the Total is :", total,"/ 500.0")
# print(" the Percentages is", percentage,"%")

# if (percentage>=60):
#     print("Grade A")
    
# elif (percentage>=50):
#     print("Grade B")

# elif (percentage>=40):
#     print("Grade C")
    
# else:
#     print("Grade D")

# Last_unit=float(input("Enter the last month unit :"))
# Current_unit=float(input("Enter the current month unit :"))

# total_unit=0
# total_unit=Last_unit+Current_unit
# print(total_unit)

# if (total_unit<=100):
#     print(total_unit*2)
    
# elif (total_unit<=200):
#     print((total_unit*2)+
#           (total_unit-100)*3)

# elif (total_unit==300):
#     print((100 * 2 )+
#           (100 * 3 )+
#           (total_unit-200)*4)


# elif (total_unit<=300):
#     print((100 * 2)+
#           (100 * 3)+
#           (100 * 4)+
#           (total_unit-300)*5)


# num = int(input("Enter a number: "))

# factorial = 1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)


# number=int(input("Enter the number : "))
# for i in range(1,11):
#    print(number,"x",i,"=",number*i)


# number = int(input("Enter the number : "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,number):
#    sum=a+b
#    a=b
#    b=sum
#    print(sum)

# Python program to find smallest
# number in a list

# l=[ int(l) for l in input("List:").split(",")]
# print("The list is ",l)

# min = l[0]
# max = l[0]
# for i in range(len(l)):
#    if l[i] < min:
#       min = l[i] 
#    else:
#          max = l[i]
        
# print("The minimum element in the list is ",min)
# print("The maximim element in the list is ",max)


# n=int(input("Enter the num :"))
# sum=0
# for i in range(1,n+1):
#    sum = sum + (i * i)
# print("sum of square is :",sum)


# n=int(input("Enter the number of terms: "))
# sum1=0
# for i in range(1,n+1):
#     sum1=sum1+(1/i)
# print("The sum of series is",round(sum1,2))

# def factorial(n):
#     f=1
#     for x in range(2, n+1):
#         f = f*x
#     return f
# n = int(input("Enter value of n: "))
# sum = sum([i/factorial(i) for i in range(1, n+1)])
# print(sum)


# n=1234
# n=int(n/10)
# n=n*10
# n1=int(n%100)
# n=int(n/1000)
# n=n*10
# n=str(n)+str(n1)
# print(n)
