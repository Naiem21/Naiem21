# num=int(input("Enter the number of digits : "))
# sum=0
# for i in str(num):
#     sum += int(i)
# print("The sum of digits is " , sum)


# digits= input("Enter the number of digits : ")
# num = str(digits)
# frist_num = int(num[0])
# second_num = int(num[-1])
# sum_of_digits = frist_num + second_num
# print("The sum of digits is " , sum_of_digits)


# list=[8,3,5,2,0,1,4]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print("The reverse of list is :",list)


# num=int(input("Enter the number : "))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print("The factorial of number is :",factorial)



# num=int(input("Enter the number of terms :"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,num):
#     sum=a+b
#     a=b
#     b=sum
#     print("The series is : " , sum)



# n=1234
# n=int(n/10)
# n=n*10
# n1=int(n%100)
# n=int(n/1000)
# n=n*10
# n=str(n)+str(n1)
# print(n)


# number=input("Number of digits : ")
# if number==number[::-1]:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")

# my_string =input("Enter the string : ")
# str=""
# for i in my_string:
#     str=i+str
# print(str)

# set1={1,2,3}
# set2={4,5,6}
# set1.update(set2)
# print(set1)


# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# res_list=[]
# for i in range(0,len(list1)):
#     res_list.append(list1[i]+list2[i])
# print (res_list)


# list1=[1,2,3]
# list2=[4,5,6]
# # for i in list2:
# #     list1.append(i)
# list1.extend(list2)
# print (list1)