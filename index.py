"""
print("hello world")
import sys
print(sys.version)
if 5 > 3:
    print("five is greater than three")
"""
# x=5
# y="hello world"
# print(type(x))
# print(type(y))

# students = ["raghu","varshini","bhumika","ramya"]
# w,x,y,z = students
# a = "they are from 27r batch"
# print(w)
# print(x)
# print(y)
# print(z)
# print(a)
# x="varshini"
# y="is"
# z="from AP"
# print(x,y,z)
# x="27r - batch"
# def myfunc():
#     print("varshini is from " + x)
# myfunc()
# x={"name":"varshini","batch":"27r"}
# print(x)
# x={"varshi","raghu",1,5}
# print(x)
# for i in "varshini":
#     print(i)
# str1="10"
# str2="10"
# print(id(str1))
# print(id(str2))
# print(2 or 3)
# print(3 or 2)
# print(-2 or 0)
# print(True or 0)
# print(-2 and 0)
# 1011-b,hex,oct
# 1567-hex,oct
# 1AEB-hex
# 1*0+1*1+
# print(13|16)
# print(~12)
# print(4<<5)
# print(5>>4)
# Decimal   Binary
# 0         0
# 1         1
# 2         10
# 3         11
# 4         100
# 5         101
# 6         110
# 7         111
# 8         1000
# 9         1001
# 10        1010
# 11        1011
# 12        1100
# 13        1101
# 14        1110
# 15        1111
# 16        10000
# 17        10001
# 18        10010
# 19        10011
# 20        10100
# range(0,20)
# for i in range(0,20):
#  if i % 2 == 0:
#     print(i,"even")
#  else:
#     print(i,"odd")
# num1 = 0
# if num1 >=0:
#     print("something")
# elif num1 ==0:
#     print("zero") 

# # Number of rows
# rows = 5

# # Loop to generate the pattern
# for i in range(1, rows + 1):
#     print('*' * i)
# i=1
# while i< 30:
#     # if i% 2==0:
#     print(i)
#     i+=2

# i=-10
# while i<20:
#     if i>0:
#       print(i,"positive")
#     elif i==0:
#         print(i,"zero")
#     else:
#         print(i,"negative")   
#     i+= 1
# count = 0
# for i in range(0, 20):
#     count+=1
#     if i==7:
#       continue
#     print(i)  
# print("count", count)
# count =0
# for i in range(0, 20):
#     count+=1
#     if i>=7:
#       break  
#     print(i)
# print("count", count)  

# for i in range(0, 20):
#     print(i)
#     continue
#     print(i)

# unit=100
# if unit<350:
#    if unit<=200:
#       if unit<=100:
#         print(unit*-5)
#       else:
#         print(0)
#    else: 
#       print(unit*10)
# else:
#     print(unit*20) 

#nested loop 02/01/2025
# for i in range(1,11):
#     for j in range(1,31):
#         if (i==7 or i==8)and j>15:
#             continue
#         print(i,j)
    
# for i in range(1,11):
#     for j in range(1,31):
#         if (i==7 and j>15)or(i==8 and j>20):
#             continue
#         print(i,j)

# for i in range(1,11):
#     if i>6:
#         continue
#     for j in range(1,31):
#         print(i,j)        
# count=0 
# for i in range(1,11):
#     print(i)
#     for j in range(1,21):
#         count+=1
#         break
# print(count)
# count=0
# for i in range(1,11):
#     j=1
#     while j < 21:
#         print(i,j)
#         j+=1
# print(count)
# count=0
# i=0
# while i<10:
#     i=i+1
#     j=1
#     while j<16:
#         print(i,j)
#         j+=1

#03/01/2025

# list1=[1,2,3.4,-57,100,123,-99]
# list =sum(list1) 
# print(list)
# list1=[1,2,3.4,-57,100,123,-99]
# sum=0
# count=0
# for i in list1:
#     sum+=i
#     count+=i
#     print(sum)
# if count==0:
#     print("empty")
# else:
#     print(sum/count)

# list2=[[1,5,0.9],[2,4,89,-2],[],[-32,9.32]]
# sum=0
# count=0
# for i in list2:
#     for j in i:
#         sum+=j
#         count+=j
#         print(j)
# if count==0:
#     print("empty list")
# else:
#     print(sum/count)   
# def sum(a,b,*c):
#     print(type(c))
#     print(c)
#     sum = a+b
#     for i in c:
#         sum+=i
#     return sum
# sum(1,3,6,9,4)

#04/01/2025
#Functions - void, normal function
#position 
#Arbidary arguments, keywords arbitary arguments

# def sum (**args):
#     print(type(args))
#     print(args)
#     sum=0
#     for i,j in args.items():
#         sum+=j
#     return sum
# print(sum(num1=5,num2=6,num3=7,num4=8,num=9))

# num1=10
# def trail():
#     b=35
#     global num1
#     num1=25
#     print(b)
#     print(num1)
# trail()
# print(num1)    

# for i in range(0,11):
#     if i%2==0:
#         print("it is even")
#     else:{
#         print("it is odd")
#     }    

# a=[1,2,3,5,9]
# x=max(a)
# print(x)

#07/01/2025
#recursion -->
# def fact(n):
#     if n==1:
#         return 1
#     temp=fact(n-1)
#     print(temp)
#     return n*temp
# res=fact(5)
# print(res)

# def ab(n):
#     if n==0:
#         return
#     ab(n-1)
#     print(n)  
# ab(10)  #1,2,3......n

# def ab(n):
#     if n==0:
#         return
#     print(n) 
#     ab(n-1) 
# ab(10)  #n......3,2,1

# rows=6
# for i in range(1,rows+1):
#     print('*' *i)
# def room(func):
#     def wall():
#         print("balloons are decored")
#         func()
#         print("wappers are hanged")
#     return wall
# @room        
# def printer():
#     print("printing...")
# printer()

# set1={1,2,3,0.5}
# set2={1,4,7}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.isdisjoint(set2))
# set1.add('raghu')
# set1.remove('varshini')
# set1.discard(3)
# set1.pop()
# set1.clear()
# print(set1)

# leap year
# year = int(input("enter year"))
# if (year % 100 != 0 and year %4 == 0) or year % 400 == 0:
#     print("leap year")
# else:
#     print("not a leap year")    

# str1 = input("enter the single charater - ").lower()
# if len(str1) > 1 or len(str1) == 0:
#     print("i want run the code")
# else:
#     if str1 in 'aeiou':
#         print("Vowels")
#     elif str1.isalpha():
#         print("Consonants")   
#     else: 
#         print("Neither")
  
# num = 12345
# temp = num
# sum = 0
# count = 0
# rev_num = 0
# while num > 0:
#     rem = num %10
#     sum +=rem
#     count +=1
#     rev_num = rev_num * 10 + rem
#     num = num // 10
# print(rev_num) 
# if temp ==rev_num:
#     print("palindrome") 

# user_account = "varshini"
# user_password = "chinni@123"
# allowed_attempts = 3
# while allowed_attempts > 0:
#     print("enter user name")
#     print("enter user password")
#     user_input = input("enter username - ")
#     user_input = input("enter password - ")
#     if user_account == user_input and user_password == user_input:
#         print("login successful")
#         break
#     else:
#         print("wrong credentials")
#         allowed_attempts-=1

# user = input("enter a square or cube or exit") 
# while True:
#     if user == "square":
#         user_num_input = float(input("enter a number to square - "))
#         print()
#     # elif user == "cube":
#     #      user_num_input = float(input("enter a number to cube - "))   
#     elif user == "exit":
#         break
#     else:
#         print("Invalid input")  


# fabinnoci series
# num = int(input("enter the number:"))   
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for i in range(2,num):
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#     print(temp)

# armstrong number
# num = int(input("enter a number:"))
# lower = 100
# upper = 10000
# for i in range(lower,upper + 1):
#     temp = i
#     temp_str = len(str(i))
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum += rem ** temp_str
#         temp = temp // 10
#     if i == sum:    
#         print(i,"armstrong") 

# 13/02/2025
# def even_odd(x):
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# res = even_odd(4)
# print(res)  
# armstrong number
# def check_armstrong(num1):
#     temp = num1
#     res = 0
#     while temp >= 0:
#         rem = temp % 10
#         res += rem ** len(str(num1)) 
#         temp = temp // 10
#     return res == num1
# lower_bound = int(input("enter lower number:"))
# upper_bound = int(input("enter upper number:")) 
# for i in range(lower_bound,upper_bound + 1):
#     if check_armstrong(i):
#         print(i)

# def print_armstrong_range(lower_bound,upper_bound):
#     for i in range(lower_bound,upper_bound + 1):