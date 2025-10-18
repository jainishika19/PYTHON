#******checking whether no is prime or not*****
# num=int(input("enter a number:"))
# if num<=1:
#     print("not a prime number")
# else:
#     is_prime=True
#     for i in range (2,num):
#         if num % i== 10:
#             is_prime=False
#             break
#     if is_prime:
#         print("prime number")
#     else:
#         print("not a prime")

# #******checking that btw 10 and 50 how many prime no.s are there
# count=0
# print("prime numbers between 10 and 50 are:")
# for num in range(10,51): #from 10 to 50
#     if(num>1):
#         for i in range(2,num):
#             if num%i==0:#checking that num is divisible by 2 upto by its own 
#                 break #(if num is divisible by i then it is not prime and we go out 
#             #from the loop and again go to the starting of the loop)
#         else:#(this else is of for loop not of if loop)
#                 print(num, end=" ")
#                 count+=1
# print("\ntotal prime numbers:",count)

#*******sum of ALL digits of any number*****
# num=125
# sum_of_digits=0
# while num>0:
#     digit=num%10
#     sum_of_digits=sum_of_digits+digit
#     num=num//10
# print("sum of digits:",sum_of_digits)

#*****checking how many numbers are there btw 1-500 whose sum of digits
#of these numbers is 10
# for num in range(1,501):
#     temp=num#create a temporary variable to hold the current no without 
#     #modifying the original no(num)
#     sum_of_digits=0
#     while(temp>0):
#         digit=temp%10
#         sum_of_digits+=digit
#         temp=temp//10

#     if(sum_of_digits==10):
#         print(num)#now print the original num








