# # printing numbers backwards
# def show(n):
#     if n==0:
#         return#when n==0 it return t0 below condn and if any condn
#         #remains it read that condn and execute
#     print(n)
#     show(n-1)
#     print("end")#like if we write this condn so at the end of the 
#     #program this line runs until call stack is empty

# show(5)



# 1)FIBBONACCI SERIES
# def fibonacci(num):
#     return num if num <= 1 else fibonacci(num-1) + fibonacci(num-2)
#     # if(num==1):
#     #     return num
#     # elif(num==0):
#     #     return num
#     # elif(num<1):
#     #     return 0
#     # else:
#     #     return fibonacci(num-1)+fibonacci(num-2)

# # nterms = 10
# nterms=int(input("enter n terms:"))
# print("Fibonacci sequence")
# for num in range(nterms):
#     print(fibonacci(num))



# 2) factorial of number
#python program to print factorial of a number using recurion

# def factorial(num):
#     """
#     This is a recursive function to find the factorial of a given number
#     """
#     return 1 if num == 1 else (num * factorial(num-1))

# num = 5
# print ("Factorial of {0} is {1}".format(num, factorial(num)))
# #the line "Factorial of {0} is {1}".format(num, factorial(num)) ---is a string that
# # contains placeholders in place of {0} num value comes and in place of {1} factorial(num) 




# SUM OF FIRST N NATURAL NUMBERS

# def sum(n):
#     if(n==0): 
#         return 0
#     return n+sum(n-1)

# print(sum(10))





# #TO PRINT ALL ELEMENTS IN A LIST
# def print_list(list,index=0):#by default we pass index=0 in parameter
#     if(index==len(list)):
#       return
#     print(list[index])
#     print_list(list,index+1)

# numbers=[1,2,3,4]
# print_list(numbers)
    
 
 