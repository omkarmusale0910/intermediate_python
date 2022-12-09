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
# tup=("omkar",20,True) # here parenthisisi is optional tup="omkar",20,True
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


# set  it is a unordered ,mutable and strore unique element
# declearation of set is done as fllowing two ways
# s1=set([1,2,3])
# S1={1,2,3,1,2} #here only single element is present rather than key value as in dic and element is seprated by ,
# # and all element is in {} this bracket
# print(S1) # print{1,2,3} not print{1,2,3,1,2} only store unique element

# # if we want to declear set with no element than
# set1={}
# print(type(set1)) # this treate as a dictionery
# # correct way
# set1=set()
# print(type(set1))

# add an remove element from set
# add
# S1.add(4)
# S1.add(5)
# S1.add(4)
# print(S1)
#
# S1.remove(4)
# # S1.remove(6) # is value is not present in set and we want to remove then it throw an error
# # there is another method to delete value from set
# S1.discard(1)
# S1.discard(9) # 9 is not present in set also it dose not throw an error
# print(S1)

# iterate over set with
# for i in S1:
#     print(i,end=" ")
# else:
#     print()

# even={0,2,4,6,8,10}
# odd={1,3,5,7,9}
# prime={2,3,5,7}
# # unoion of set
# u= even.union(odd)
# print(u)
# # intersection of set
# i=even.intersection(prime)
# print(i)
# # set diff setA-setB
# diff=odd.difference(prime)
# print(diff)

# c=even+odd  + concatination only work on list
# print(c)

# # subset and super set
# print(u.issuperset(odd))
# print(even.issubset(u))
#
# # finding sets are disjoint or not
# inter_even_odd=even.intersection(odd)
# print(inter_even_odd==set())
# # or with disjoint method
# if even.isdisjoint(odd):
#     print("Yes")

# # copying set
# # U=u  # this both  pointing to same memory location
# # change in one set can cause change in another set
# # correct method is
# # U=u.copy()
# U=set(u)
# U.add(100)
# print(U)
# print(u)

# frozenset this set is imutable update can not work only intersection,union operation is work
# fs=frozenset([1,2,3,4,5])
# print(fs)
























