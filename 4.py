# 28|10|2025 Tuesday
# start of the training
# 
# 
# everything in python is in the form  of object.
# import keyword
# . means ke andar
# print(keyword.kwlist)
# kwlist is a File
# you can also make a keyword of you own
# there can be also user defined fns ,DS,as per the requirements of your company
# special character can't be used in the name of an identifier but WHY?
# how and why python identifies the datat ype itself code history behind this
x=2 
y=2
print(id(y)) #addr of y
print(id(x))#addr of x
# in python whenever two variables have same value then their addr will be same 
#is it also possible in c and c++? 
# Docstring can be print """this docstring can be printed? in the output or just a multiline comment ans me ishika"""
# indentation :1 tab or 4 spaces 
a=7 
b=6
print("The value of a is {} and b is {}".format(a,b))
# indexing also possible
a=9 
b=87
print("The value of a is {1} and b is {0}".format(a,b))
# a = int(input(" "))
# b =input("HEllow")
# input fn by default string leta hai
# integer lene keliye int laga na padega pehle
# use while loop when you don't know how many time it will iterate
# for loop when you know

# number = [1,2,3,4,5]
#else bhi execute hoga but while ke badd
#itratiing ovr the last element
# index = 0 
# while index<len(numbers):
#     print(numbers[index])
# else:
#     print("list is over now")
# for i in list
# for i in range(10)
# range takes 3 params starting ,ending , steps
# starting and steps are optional
# by default starting is 0
# by default step is 1
# ending is mandatory
# ending has the curse of exclusivity means loop will run till n-1 times

numbers=[1,3,6,9]
#iterating over the last
for items in numbers
    print(items)
else:
    print("no item left")#else will run after for worked
    
numbers = [2,4,6,8,10,5,12]
for num in numbers:
    if num==4:
        continue
    print(num)
else:
    print("in the else-block")
print("Outside the for loop")

# FUNCTIONS 
# increase code reusability
# u call a fn
# from def we define a fn
# ;def is a statement from which python's interpret understand it as a fn
# def fn_name(param)
    "fn body"
don't name fn on name of keywords

# str is for prevention 
def greet(name):
    """I am the doc string of this
    fn , hey ishika , aaj kyun ni aai?
    haan!"""
    print("HELLO"+str(name))
greet(ishika)#fn call
""" docstring type multicomment"""
print(greet._doc_)#print doc string of the fn greet

def get_sum(lst):
    """this is the 
    docstring
    """
    #initialize sum
    _sum=0
    #iterating over the last
    for num in lst:
        _sum +=num
    return _sum

s = get_sum([3,5,3,6])
print(s)
# /what is a param and a arguments
# is param and argument are same or different
(5,6)are passing arguments
(a,b)are parameters
def get_sum(a,b)"""
"""
get_sum(5,6)