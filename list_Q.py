# #printing index of numbers whose pair sum is ==6 in 
# lst=[7,5,3,4,9,2,5]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==6:
#             print(lst[i],lst[j]) #print numbers
#             print(i,j) #print index




# 2) WAP to ask the user to enter names of their 3 fav movies and store them in a list
# movies=[] #empty list
# mov1=(input("enter 1st movie :"))
# mov2=(input("enter 2nd movie :"))
# mov3=(input("enter 3rd movie :"))

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# or we can directly store and append both
# movies=[]
# movies.append(input("enter movie 1:"))
# movies.append(input("enter movie 2:"))
# movies.append(input("enter movie 3:"))
# print(movies)


# 3) WAP to check if a list contains a palindrome of elements 
# ----palindrome are like word "eye" -if we read it from starting and as well as from last
# it pronounce same
# example of palindrome list--[1,2,3,2,1]

list1=[1,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")


grade=["C","D","A","A","B","B","A"]
print(grade.sort())#it prints none
grade.sort()
print(grade)