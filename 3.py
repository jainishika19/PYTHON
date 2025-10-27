# print all the numbers whose sum and product of all digits are equal

# for i in range(100,1000):
#     sum=0
#     product=1
#     num = i #store original no. in num variable
#     while i>0:
#         sum=sum+i%10 #sum of digits
#         product=product*(i%10) #product of digits
#         i=i//10
#     if sum==product:
#         print(num)  


# *****this program can also be written as 
for i in range(100,1000):
    # first separate all the digits
    a=i%10 #getting 3rd digit
    b=(i//10)%10 #getting 2nd digit
    c=i//100 #getting 1st digit

    # now we find sum ,product and check
    if a+b+c==a*b*c:
        print(i)