# double=lambda x:x*2
# print(double(8))

#*****TO CHECK IF NO IS EVEN OR ODD******
#BY normal fntn
# def check_even_odd(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")
# n=int(input("enter no:"))
# check_even_odd(n)


# BY lambda fntn
# int = lambda x:"even" if x%2==0 else "odd"
# print(int(5))
# x=int(input("enter number"))
# print(int(x))

# NOW USING FILTER 
# FILTER FNTN----return only true values

# lst=[1,2,3,4,5]
# even_lst=list(filter(lambda x:(x%2==0),lst)) #here only those values return which satisfy inside
# # (bracket) condn as here filter fntn is 
# print(even_lst)


# # ***using map() fntn--take one by one values and return
# lst=[1,2,3,4,5]
# new_lst=list(map(lambda x:x**2,lst))#here passsing fntn inside fntn
# print(new_lst)


# *using reduce fntn
# from functools import reduce
# lst=[1,2,3,4,5]
# product_lst=reduce(lambda x,y:x*y,lst)
# print(product_lst)

# num=int(input(""))
# sum=0
# int=lambda num:sum+(num%10)
# num=num/10

# print(int(num))


num = int(input("Enter a number: "))
sum_digits = lambda n: 0 if n == 0 else n % 10 + sum_digits(n // 10)
print("Sum of digits:", sum_digits(num))

