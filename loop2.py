#Q1
# for i in range(0, 4):
#     for j in range(0, 2):
#         print("*", end="")
#     print()

#Q2
# for i in range(0, 4):
#     for j in range(0, 3):
#         print("*", end="")
#     print()

#Q3
# for i in range(0, 5):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

#Q4
# for i in range(0, 5):
#     for j in range(5-i):
#         print("*", end="")
#     print()

#Q5
# for i in range(0,4):
#     for j in range(1,5-i):
#         print(j,end="")
#     print()   
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#Q6
# for i in range(97,101):
#     for j in range(97,i+1):
#         print(chr(j),end=" ")
#     print()

#level2

#Q1

# for i in range(0,4):
#     for j in range(4-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

#Q2

# for i in range(0,4):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(2*(4-i)-1):
#         print("*",end=" ")
#     print()    

#Q3
# for i in range(0,5):
#     for j in range(5-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

#Q4
# for i in range(0,3):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(0,3):
#     for j in range(3-i-1):
#         print("*",end="")
#     print()

#Q5
# for i in range(0,3):
#     for j in range(i + 1):
#         print(j+1, end="")
#     print()
# # lower triangle
# for i in range(0,3):
#     for j in range(3 - i - 1):
#         print(j+1, end="")
#     print()


#Q6
# num=int(input("Enter the number : "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,num):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)

#Q7

# num = int(input("Enter a number: "))
# flag = False
# if num > 1:
    
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")