# name=input("what is your name?")
# print(name)
# print("hello "+ name)#concatenation--adding of 2 words/string/...etc


# old_age=input("enter your age:")
# # new_age=old_age+2 ---but here error bcs we try to add string with integer
# # as old_age is taken as string
# new_age=int(old_age)+2
# print(new_age)


# num=18
# print(float(18))#covert int to float


first=input("enter 1st num:")
second=input("enter 2nd num:")
sum=first+second
# print(sum)--it prints 45(if no,s are 4,5)
#because first and second is taken as string not integer
sum=int(first)+int(second)
print(sum)
#print("the sum is:"+sum)--error as sum taken as string can't concatenate
print("the sum is:"+str(sum))