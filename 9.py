# calculator

print("select option")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter your choice:"))
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
if(choice==1):
    print("addition is:" ,a+b)
elif(choice==2):
    print("subtraction is:",a-b)
elif(choice==3):
    print("multiplication is:",a*b)
else:
    print("division is:",a/b)
