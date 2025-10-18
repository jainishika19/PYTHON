#get all keywords in python
#import keyword
#print(keyword.kwlist)
#print("total no of keywords",len(keyword.kwlist))
#_a=10
#@a=10
#x=3
#print(id(x))

# slicing
# s="this is the tutorial"
# print(s[:5])
# print(s[5:])

# ******greatest of 3 numbers******
# a=29
# b=49
# c=50
# if a>=b and a>=c:
#    greatest = a
# elif b>=c and b>=a:
#    greatest =b
# else:
#    greatest =c
# print("the greatest number is:",greatest)
# print("the greatest number is{}:",format(greatest))//same as this

# also by ---
# a=5
# b=5
# c=5

# greatest =max(a,b,c)
# print("the greatest number is:",greatest)

# ******while loop*******
# numbers=[1,2,3,4,5]
# #iterating over the list
# index=0
# while(index<len(numbers))
#     print()



#******checking whether prime or not***********
# num = int(input("Enter a number: "))  #convert string to int
# isDivisible = False;

# i=2;
# while i < num:#//let i=3 & num=77
#     if num % i == 0:#77%3==0
#         isDivisible = True; #true
#         print ("{} is divisible by {}".format(num,i) )#77 is div by 3
#     i += 1;#now i=4
    
# if isDivisible: #num 77 is div by 3
#     print("{} is NOT a Prime number".format(num))  #so not a prime
# else:
#     print("{} is a Prime number".format(num))



#*********sum of digits of a number*********
#num=123
# num=int(input("enter a number:"))
# sum=0
# while(num>0):
#    digit=num%10
#    sum+=digit
#    num=num//10 #in division // bcs it gives integer answer while single '/' gives decimal value
# print("sum is ",sum) #int(sum) for integer value of sum in o/p  

#********printing all possible numbers whose sum of each digits =10 btw 1 to 500
# print("number whose sum of digits is 10:")
# int num in range(1,101)

int num in range(100,999)
n=num
while(num>0)