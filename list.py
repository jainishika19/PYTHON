# #list

# info=[34,55,"maths"]
# print(info[0])


# info=[34,55,"maths"]
# print(info[-1]) # -1 means starting from last so it prints maths 
# # print(info[-4])#error as list is out of range/

# # if we want only 2 elements of starting in our list so ---

# info=[34,55,"maths"]
# print(info[0:2]) #prints [34,55] as here only 0th and 1st index element is included
# print(info[1:3]) 



# marks=[44,22,56]
# marks.append(77) #append adds element in list at last
# print(marks)
# marks.insert(0,59) #it adds 59 at the 0th index
# print(marks)
# print(99 in marks) #false
# print(len(marks)) #5 elements


# classwork

fruits_lst=['mango','banana','grapes','apple','pomegranate']
# print(fruits_lst)#complete list print
for i in fruits_lst:
    print("i like",i)
print("length of list is:",len(fruits_lst))#length fntn -- to find length
fruits_lst.append('pineapple')
print(fruits_lst)
fruits_lst.insert(1,'kiwi')
fruits_lst.insert(5,'kiwi')
print(fruits_lst)

# to remove any element
fruits_lst.remove('kiwi')#remove-by item's name
print(fruits_lst)#kiwi is 2 times in list so it remove 1st kiwi
#removes 1st occurence element always
fruits2=['orange','guava']
# fruits_lst.append(fruits2)
# print(fruits_lst)#it prints list inside list
fruits_lst.extend(fruits2)
print(fruits_lst)

# to remove item based on index--use 'del'
del fruits_lst[2] #delete --by indexing//while remove by items name
print(fruits_lst)

#or we can use pop method
a=fruits_lst.pop(3)#it stores what element is deleting
print(a)
print(fruits_lst)
