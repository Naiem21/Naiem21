#Q1
# for i in range(22,55):
#     if i % 2 == 0:
#         print(i)

#Q2
# for i in range(44,62):
#     if i % 2 != 0:
#         print(i)

#Q3
# number =int(input("Enter the number of value : "))
# temp=str(number)
# t1=temp+temp
# t2=temp+temp+temp
# count=number+int(t1)+int(t2)
# print(count)

#Q4

# number = int(input("Enter the number : "))
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
#     print(fact)

#Q5
# sum=0
# for i in range(11,22+1):
#     sum=sum+i
#     print(sum)

#Q6
# sum=0
# for i in range(1,20+1):
#     if i % 2 == 0:
#         sum=sum+i
#         print(sum)

#Q7
# n=int(input("Enter the number : "))
# for i in range(1,n+1):
#     print(i)

# #Q8

# print("Alphabet from a-z:")
# for i in range(97,123):
#     print(chr(i),end=" ")
    
# print("Alphabet from A-Z:")
# for i in range(65,91):
#     print(chr(i),end=" ")

#Q9
# number=int(input("Enter the number : "))
# for i in range(1,11):
#     print(number,"X",i,"=",number*i)

#level2
#Q1
# number=int(input("Enter the number of digits : "))
# count=0
# while (number>0):
#     count+=1
#     number=number//10
#     print(count,end=" ")

# number=input("Enter the number of digits : ")
# print(len(str(number)))

#Q2
number=input("Enter the number of digits : ")
sum=0
for i in number:
    sum=sum + int(i)
print(sum,end=" ")

#Q3

# number=int(input("Enter the number of digits : "))
# a=number[::-1]
# print(a,end=" ")
# rev_num=0
# while (number>0):
#     remainder=number%10
#     rev_num=(rev_num*10)+remainder
#     number=number//10
#print(rev_num,end=" ")

#Q4
# num=int(input("Enter the number : "))
# power=int(input("Enter the power: "))
# CP=1
# for n in range(power):
#     CP = CP*num
# print("the power of number is:",CP)
    
#Q5
# num=input("Enter the number :")
# i=0
# for i in range(len(num)):
#     if num[i]==num[-1-i]:
#         print("pelindrom")
#         break
#     else:
#         print("not pelindrom")
#         break

#Q6
# num=int(input("Enter the number : "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,num+1):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)

# def printNumber(n):
#     if n > 0:
#         printNumber(n-1)
#         print(n,end=' ')
# n=50
# printNumber(n)
