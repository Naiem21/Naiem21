# print('"hello" "world"')

# print("line A\n lineB\n lineC\n lineD\n")

# print("name\tnaiem")

# print("this is\ backslash")

# print("this is backslash\\")

# print("this is backslash\\\\")

# print("hell\blo")

# print("this is /\\/\\/\\/\\ mountains")

# print("this is \tmountains")

# print("\\\" \\n \\t \\\'")

# print(2+3*4)

# print(2/4)

# print(2//4)

# print(4//2)

# print(2**4)

# print(2**0.5)

# round(2**0.5)
# print(round(2**0.5,4))


# name='naiem'
# age=22
# print(f"hello {name} youre age is {age+2}")


# num1=int(input("Enter the first no. : "))
# num2=int(input("Enter the sceond no. : "))
# num3=int(input("Enter the third no. : ")) 
# num1,num2,num3 = input("Enter the three comma separated :").split(",")
# print(f"average of three num :{(int(num1)+int(num2)+int(num3))/3}")
# ave=(num1+num2+num3)/3
# print(ave)


# NAME="naiemkhan"
# print(NAME[-3])
# print(NAME[0:5])


# name=input("enter the name : ")
# a=name[::-1]
# print(a)
# print(f"reverse of the yuor name is {name[::-1]}")

# name=input("enter the name : ")
# print("hello"+" "+ name)
# age=input("what is your age? ")
# print("your age is "+" "+ age)

#name = 'naiemkhan'
#print(len(name))
#print(name.upper())
#print(name.title())
#print(name.count("h"))



# name , char =input("Enter the commma supretted name and char :").split(",")
# print(f"name lantgh is {len(name)}")
# print(f"char count is {name.strip().lower().count(char.strip().lower())}")
#print(f"char count is {name.count(char)}")

 
#name="    na    iem    "
#dots="..........."
#print(name+dots)
#print(name.lstrip()+ dots)
#print(name.rstrip()+ dots)
#print(name.replace(" " , "")+dots)



#string="he is a good batter but he is not good captian "
#print(string.replace(" " , "_"))
# print(string.replace("is","was",2))
#pos1=string.find("is")
#pos2=string.find("is" , pos1+1)
#print(pos2)



#name = 'naiemkhan'
#name=input("Enter the user name : ")
#print(name.center(len(name)+8,"*"))

# name="Naiem"
# name+=" Khan"
# print(name)
# age=22
# age+=1
# print(age)

#age=int(input("Enter the age :"))
#if age >=14:
    #print("you are above 14 : ")
   
   
    
#x=18
#if x > 18:
    #pass
  
  
    
#age=int(input("Enter the age :"))
#if age >=18:
    #print("you are aligiable for vote : ")
#else:
    #print("you are not aligiable for vote :") 
   
   
    
#wining_num=27
#user_num=int(input("Enter the num b/w 1 to 100 : "))
#if user_num  == wining_num:
    #print("you win !!!! ")
#else:
    #if user_num < wining_num:
        #print("too low")
    #else:
        #print("too high")
        
    

#name=input("Enter the name : ")
#age=int(input("Enter the age : "))
#if  (age >= 10 and name[0]=="a" or name[0]== "A"):
   # print("you can watch coco movie")
#else:
    #print("you can not watch coco movie")
    

#age=int(input("Enter the your age : "))
#if age<0:
    #print("you are not a human : ")
#elif 0<age<=3:
    #print("your ticket is free : ")
#elif 4<age<=10:
    #print("your ticket is 150 : ")
#elif 11<age<=60:
    #print("your ticket is 250 : ")
#else:
    #print("your ticket is 200 : ")
   
    
# name=input("Enter the name :")
# char=input("Enter the character :")
# if char in name: 
#     print("char present in name ")
# else:
#     print("not present in name ")

# i=1
# while i<=10:
#     print("hello world")
#     i=+1

# total = 0
# i = 1
# while i <= 10:
#     total=total+i
#     i=i+1
# print(total)

# name=input("Enter the name :")
# if name:
#    print(f"youe name is {name}")
# else:
#     print("you did not type anything")
 
 
#n=int(input("Enter the number :"))
#total=0
#i=1
#while i <=n:
    #total+=i
    #i+=1
#print(total)

#n=(input("Enter the number :"))
#total=0
#i=0
#while i <len(n):
    #total+=int(n[i])
    #i+=1
#print(total)


# n=(input("Enter the your name  :"))
# i=0
# while i <len(n):
#     print(f"{n[i]} : {n.count(n[i])}")
#     i+=1


#for i in range (10):
    #i+=1
    #print(i)

#num=int(input("Enter the Digits : "))
#for i in range (0,num):
    #print(f"Hello world: {i}")
    
# num=int(input("Enter the digits :"))
# total=0
# for i in range (1,num+1):
#     total+=i
# print(total)

# num=input("Enter teh digits :")
# total=0
# for i in range (0,len(num)):
#     total+=int(num[i])
# print(total)

# name=(input("Enter the your name  :"))
# temp=""
# for i in range (0,len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#     temp+=name[i]
    

#num=int(input("Enter the Digits :"))
#for i in range (0,num):
    #if i==5:
        #break
        #continue
    #print(i)


#wining_num = 43
#guess = 1
#user_num = int(input("Enter the number b/t 1 to 100 :" ))
#game_over = False
#while not game_over:
#    if user_num == wining_num:
    #    print(f"You win , You guess number in  {guess} times :")
        #game_over = True
    #else:
        #if user_num < wining_num  :
            #print(" Too low guess !!!")
            #guess+=1
            #user_num=int(input("guess again :"))
        #else:
            #print("Too high guess !!!")
            #guess+=1
            #user_num=int(input("guess again :"))


#for i in range(10,0,-1):
#    print(i)


    
#def add_three(a,b,c):
#    return a + b + c
#print(add_three(5,5,5))   

# def last_char(name):
#    return name[-1]
# print(last_char("naiem"))


# def odd_even(num):
#     num=int(input("Enter the number :"))
#     if num %2==0:
#         return"even"
#     return"odd"
# print(odd_even("num"))


# def greater(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1=int(input("Enter the 1st num : "))
# num2=int(input("Enter the 2nd num : "))
# bigger=greater(num1,num2)
# print(f"{bigger} is greater ")

# def add_two(num1,num2):
#     return(num1+num2)
# first_name=input("Enter the name")
# second_name=input("Enter the name")
# print(add_two(first_name,second_name))

# def is_even(num):
#     return num%2==0
# print(is_even(10))


# def greater(a, b, c):
#     if a > b:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# num1=int(input("Enter the 1st num : "))
# num2=int(input("Enter the 2nd num : "))
# num3=int(input("Enter the 3rd num : "))
# bigger=greater(num1,num2,num3)
# print(f"{bigger} is greater ")


# def greater(a, b, c):
#     if a > b:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# def new_greaterest(a,b,c):
#     bigger=greater(a,b)
#     return greater(bigger,c)
# print(new_greaterest(1,4,11))

# def is_palindrome(word):
#     # if word == word[::-1]:
#     #     return True
#     # return False
#     return word == word[::-1]
# print(is_palindrome("naiem"))
# print(is_palindrome("naman"))

# def fibonacci_seq(n):
#     a = 0   
#     b = 1
#     if n == 1 :
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a,b,end =     " ") 
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end = " ")
            
# fibonacci_seq(20)
 
 
# def rev_sentence(sentence): 
  
#     # first split the string into words 
#     words = sentence.split(' ') 
  
#     # then reverse the split string list and join using space 
#     reverse_sentence = ' '.join(reversed(words)) 
  
#     # finally return the joined string 
#     return reverse_sentence 
  
# if __name__ == "__main__": 
#     sentence=input("Enter the sentence")
#     print (rev_sentence(sentence))


# string = input("Enter the your sentence : ")
# words = string.split()
# words = list(reversed(words))
# print(" ".join(words))



# a=[10,20]
# b=a
# b+=[30,40]
# print(a)

# a=65
# print('[%c]'%a)

# a=2*2//2
# b=3//2*3
# print(a,b)

# b=30
# def fun(a,b=b):
#     return a+b
# print(fun(1))

# def fun():
#     print("fun")
# print(fun())

# def x(values):
#     values[0] = 1
# v=[2,3,4]
# x(v)
# print(v)    

# a= [0,1,2,3]
# for a[-1] in a:
#     print(a[-1])

# def fun():
#     return[i for i in  range(0,3,3)]
# print(fun())
         
# x,y=76,80
# x,y,z=1,2,3
# print(x,y,z)

# def fun():
#     return
# pass
# print(fun())


# f=lambda x: bool(x%2)
# print(f(20),f(21))

# l= [1,2,3,4]
# for i in l[::1]:
#     print(i, end=" ")

# a = 100/5
# b = 20//3
# print(a * b)

# a = max(False,-3,-4)
# b = min(a,2,7)
# print(b)

# l =list("1234")
# l[0] = l[1]=5
# print(l)

# set1= {1,2,3,int('4')}
# set2={3,str(4)}
# print(set1.union(set2))


    
# for j in range(1,8):
#     for s in range(6,j-1,-1):
#         print(" ",end="")
#     for i in range(1,2*j):
#         print("*",end="")
#     print(" ")

# age=int(input("Enter the age :"))
# if age >=18 and age < 33:
#     print("You are eligiable for vote :")
# elif age >=33:
#     print("You are not authorized for vote :")
# else :
#     print("You are not eligiable for vote ")    


# for i in range(0,10):
#     for j in range(9,i-1,-1):
#         print(" ", end=" ")
#     for k in range(1,2*i):
#         print("*", end=" ")
#     print(" ")

# for j in range(4,0,-1):
#     for s in range(3,j-1):
#         print(" ", end=" ")
#     for i in range(1,2*j):
#         print("*", end=" ")
#     print(" ")



# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print(" ")

# for i in range(0,6):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print(" ")


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print(" ")


# for i in range(1,6):
#     for j in range(i,6):
#         print(j, end=" ")
#     print(" ")   
# for i in range(6,0,-1):
#     for j in range(i,6):
#         print(j, end=" ")
#     print(" ")


# for i in range(5,0,-1):
#     for j in range(4,i-1,-1):
#         print(" ", end=" ")
#     for k in range(1,2*i):
#         print("*", end=" ")
#     print(" ")



# word = input("Enter the word : ")
# if(word== word[::-1]):
#     print("word is palindrome !!")
# else:
#     print("word is not palindrome !!")



# num = int(input("Enter the number : "))
# if(num % 2 == 0):
#     print(" num is prime")
# else:
#     print(" num is not prime")

# p=0
# n=1
# print(p)
# print(n)
# for i in range(1,9):
#     sum=p+n
#     print(sum)
#     p=n
#     n=sum
 
 
# num=int(input("Enter the no:"))
# count=0
# while num is not 0:
#     num=num//10
#     count=+1
# print(count)

# name="naiem khan"
# age=22
# print(f"hello {name} your age is {age}")