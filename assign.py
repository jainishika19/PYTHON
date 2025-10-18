#*****max of three numbers
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# c=int(input("enter 3rd number:"))
# if a>=b and a>=c:
#    greatest = a
# elif b>=c and b>=a:
#    greatest =b
# else:
#    greatest =c
# print("the greatest number is:",greatest)

#********AP
a=int(input("enter 1st term:"))
d=int(input("enter common diff:"))
n=int(input("enter no.of terms:"))
print("AP is")
for i in range(1,n+1):
    term=a+(i-1)*d
    print(term,end=" ")
nth_term=a=(n-1)*d
print("\nthe nth term of AP is:",nth_term)



