# List
# list can be created with help of list function
# list12=list()
# print(list12)

# list1=["cherry","apple","banana","orange","mango"]
# if we want to check if an item present in list or not we can use
# if "orange" in list1:
#     print("Yes")
# else:
#     print("No")

# pop method remove last element of list and return that element
# item=list1.pop()
# print(item)

# clear method deleted all the value in list
# list1.clear()

# list1.sort()
# print(list1)

# if we want same elemet in list than we can use this shortcut
# list=[0]*5
# print(list)

# str="abc"*5
# print(str)

# we can concat list
# l1=[1,2,3,4]
# l2=[("omkar","musale"),True]
# l3=[0,0,0]
# l4=l1+l2+l3
# print(l4)

# list=[1,2,3,4,5,6,7,8,9]
# list sliceing
# print(list[:])  # list[:] this method return newlist
# a=list[1:]
# print(a)
# a=list[:3]
# print(a)
# a=list[0::2]  # with ::num   here num is step size defeult step_size ids 1
# print(a)
# a=list[::-1]  # this can be used as shortcut to reverse the list
# print(a)
# a=list[2:len(list):3]  #[start:end:stride(it means step like i+=2)]
# print(a)


# coping a list
# when we used assigement oprator than both list refer to same memory location
# chaneges in one list update other list as well

# list_cpy=list
# list_cpy.append(10);  # we can write semocolen (it is not mandetory)
# print(list)
# print(list_cpy)

# we can create copy of list with copy method
# list_cpy=list.copy()
# list_cpy.append(10)
# print(list_cpy)
# print(list)

# this also used to create copy of list
# list_cpy=list[:]


# ####  List comprehention  (which is used to create new list with exiting one
# syntax for list comprehhention is
# [ expretion for ele in list (if statement (this is option)]
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[i*i for i in a]
# c=[i**i for i in a if i%2==0]
# print(a)
# print(b)
# print(c)



# tuple this are unmutable
tup=("omkar",20,True) # here parenthisisi is optional tup="omkar",20,True
# print(tup)
# # if you want to create tuple with single element than
# tup1=("omkar")
# print(type(tup1))  # this is treat as a string
# # corrct syntax for createing tuple with single ele is
# tup2=("omkar",)
# print(type(tup2))
#
# # another way to create tuple with  tuple method and pass list
# Tup=tuple([10,"omkar",True])
# print(Tup)
#
# # for checking any element in container we can use in syntax
# print("omkar" in Tup)
# print('k' in Tup[1])

# updating a tuple (tuple is Immutable but there is one method)
# tup_list = list(Tup)
# tup_list.append(2.36)
# print(tup_list)
# Tup=tuple(tup_list)
# print(Tup)
#

# slicing intuple
# print(tup[1:])

# unpaking methodology in python
# LL=[1,2,3,4,5,6]
# i1,i2,i3,*i4=LL  # if we used * than it takes all element remaing
# # other than reameing variable  * is used when number of variable on left is less than right
# print(i1,i2,i3,i4)

# working with tuple is more ifficient than working with list
# beacause it take less time to iterate and takes less space to store same element

# Dictionaries
# two ways to create dic
# dic={"name":"omkar","age":20,"city":"pune"}
# dic1=dict(name="omkar",age=20,city="pune")
# print(dic,dic1)

# for adding key value to dic
# dic["email"]="omkar@gmail.com"
# print(dic)

# for remove key val
# del dic["email"]
# dic.pop("email")
# print(dic)
# in python 3.7 only this avaible
# dic.popitem() # this pop last item which is added added

# checking if key is present or not
# if "name" in dic:
#     print(dic["name"])

# dic.keys() return list of keys
# dic.values() return list of values
# dic.items() return key,value
# for x in dic.keys():
#     print(x,end=" ")
# else:
#     print()
#
# for x in dic.values():
#     print(x,end=" ")
# else:
#     print()
#
# for key,value in dic.items():
#     print(key,value)


# while coping dic
# dic_cpy=dic
# both variable point to the same location in memory there fore
# change in one cause change in other also

# dic_cpy=dic.copy()
# dic_cpy["is_male"]=True
# print(dic_cpy)
# print(dic)

# with update method allready present keys values is chaneges and extra isdf exits than added
# suppose
# dic3={"name":"omkar", "age":22 ,"email":"abc@gmail.com"}
# dic4={"name":"pooja","age":30,"city":"pune"}
# dic3.update(dic4)
# print(dic3)

# #### IMP data type of key must be(tuple,string,int)
# it not list as a key because it can change and key must be inmutable















