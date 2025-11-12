# # split fntn 
# numbers=[1,2,3,4,5]
# slist=split(numbers)


# slicing 
# numbers=[1,2,3,4,5]
# # print(numbers[:])#by default from 0 to (length of list-1)
# # print(numbers[:3])


# # print alternate elements 
# print(numbers[::2])#2 values skip
# print(numbers[2::2])#starting from 2nd index and then skips 2 values till last
# print(numbers[6::6])


# # list extend using "+"---concatenation
# lst1=[1,2,"hello",3,4]
# lst2=['jiya','anshii',8,'snu']
# new_lst=lst1+lst2 #concatenation
# print(new_lst)


# # LIST COUNT
# num=[2,3,4,3,5]
# #frequency of 1 in a list
# print(num.count(1))
# #frequency of 3 in a list
# print(num.count(3))



# # by loop 
# num=[1,2,3,4,1]
# count=0
# for i in num:
#     if(i==1):
#         count+=1
# print(count)

# # loop through a list 
# num=[1,2,3,4]
# for element in num:
#     print(element)



# # running sum 
# lst=[1,2,3,4]
# new_lst=[]
# sum=0
# for i in lst:
#     sum=sum+i
#     new_lst.append(sum)
# print(new_lst)


# my logic😒
# lst=[1,2,0,3,0,4,5,0]
# new_list=[]
# index=-1
# for i in lst:
#         if(i==0):
#             new_list=new_list.append(new_list[index])  
#         else:
#             new_list=new_list.append
# print(new_list) 

# # q------
# # shifting all zeroes at last of the list
# lst=[1,2,0,3,0,4,5,0]
# out=[]
# zeroes=0

# for i in lst:
#     if i==0:
#         zeroes+=1
#     else:
#         out.append(i)

# #now appending zeroes at the end of list
# for i in range(zeroes):
#     out.append(0)
# print(out)


# --my thinking approach
# #to remove duplicate numbers
# num=[1,2,3,5,1,3,5]
# new_list=[]
# for i in num:
#     for j in range(i+1):
#         if(i==j):
#             num.remove(j)
# print(num)


# real sln
#to remove duplicate numbers
num=[1,2,3,5,1,3,5]
new_list=[]
for i in num:
    if i not in new_list:
        new_list.append(i)
    
print(new_list)

# # another way by set( fntn------)
# num=[1,2,3,5,1,3,5]
# new_list=set(num)
# print(new_list)
    

# string of names is given
# to count in what name 'a' comes and printt that name

str="jia","ritu","aanya"
str2=[]
ch='a'
for i in str:
    if ch in i.lower():
        str2.append(i)

print(str2)

