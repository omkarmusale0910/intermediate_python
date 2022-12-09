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
# a=list[0::2]  # with ::num   here num is step size defeult step_size is 1
# print(a)
# a=list[::-1]  # this can be used as shortcut to reverse the list
# print(a)
# a=list[2:len(list):3]  #[start:end:stride(it means step like i+=2)]
# print(a)


# coping a list
# when we used assigement oprator than both list refer to same memory location
# changes in one list update other list as well

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

# unpacking methodology in python
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
# dic.popitem() # this pop last item which is added

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
# both variable point to the same location in memory therefore
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
# it not list as a key because it can change and key must be immutable


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

# add and remove element from set
# add
# S1.add(4)
# S1.add(5)
# S1.add(4)
# print(S1)
#
# S1.remove(4)
# # S1.remove(6) # if value is not present in set & we want to remove then it throw an error
# # there is another method to delete value from set
# S1.discard(1)
# S1.discard(9) # 9 is not present in set also it does not throw an error
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

# c=even+odd  + concatination only work on list here it gives as error
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

# frozenset this set is immutable update can not work only intersection,union operation is work
# fs=frozenset([1,2,3,4,5])
# print(fs)


# ----- string -------- ordered , immutable
# # it can be in single quote double quote and triple-double quote for multi line text
# S1='omkar musael is my name \'' # "omkar musael is my name '"
# # in double quote single quote can be write without excape charater '\' wice versa
# print(S1)
# S2='omkar "'
# print(S2)

# S3="omkar prakash Musale"
# print(S3)

# mutiline_text="""My name is omker
# I am a good  boy
# I live in pune near Akurdi """
# print(mutiline_text)

# S1[0]='O' # this line give an error updation is not possible (Immutable)
# slicing of a string
# substring=S1[6:]
# print(substring)
# # reverse the string with sliceing oprator
# reverser_S3=S3[::-1]
# print(reverser_S3)

# fname,lname="omkar","musale"
# name=fname+" "+lname
# print(name)

# we can check a substring is or not
# if "mka" in S3:
#     print("yes")

# or use find method is not present return -1 ya return starting index of find substring
# print(S3.find("kar"))

# string_list=S3.split() # default argumet is " " space
# print(string_list)
# #S3.split()==S3.split(" ")   # this is not same is S3=" omkar   musale"
# # than first return ["omkar","musale"] and
# # second return ["omkar", " " ,"musale"]
# SS3="omkar,prakash,musale"
# string_list_SS3=SS3.split(",")
# print(string_list_SS3)
# print(','.join(S3.split()))
# print(' " '.join(S3.split()))

# importing time_fun library
# from timeit import default_timer as timer
#
# my_list=['omkar']*1000000
# # here we are proving join() method is much faster then + concat opration
# start=timer()
# my_str=''
# for i in my_list:
#     my_str+=i
# stop=timer()
# print(stop-start) # first opration time
#
# start=timer()
# my_str=''.join(my_list)
# stop=timer()
# print(stop-start)


# formating in string
# % ,.format() , new_python version f-Strings

# var="omkar"
# var2=312
# var1=3.124584
# my_var1="%s is good boy"%var
# print(my_var1)
# my_var2="%d value of sound speed"%var2
# print(my_var2)
# my_var3="the value of pi is %.2f"%var1
# print(my_var3)
#
# # another way of formating
# my_string="this is a value of pi {:.3f} and value of sound speed is {}".format(var1,var2)
# print(my_string)
#
#
# # newest way for formatting and one of the easiest way of formatting
# my_string= f"my name is {var} value of PI {var1} and value of sound_speed is {var2}"
# print(my_string)




# collection (counter ,nametuple,Ordereddic,defaultdic,deque)
#counter
# from collections import Counter
# str="aaaaabbbcccc"
# my_counter=Counter(str) # this return counter contain dic which contain (element,occerence)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.most_common(1)) # this return list with most occerence


# from collections import namedtuple
# # it is a dic type struct where key value is hashed to perticuler value but we can acces ele with key and iterable
# # this make class like struct first paremter as class name and second is iterable class parameter name
# Point= namedtuple('Point','x,y,z')
# Std=namedtuple('Std',["name","age","mark"])
# std=namedtuple('std',"name,age,mark")
# print(std("omkar",20,30))
# pt=Point(1,2,"ashdv")
# print(pt.x,pt.y,pt.z)
# print(pt[0],pt[1],pt[2])

# Ordereddic is a normal dic with can remember order in which element are inserted
# new python version nornal dic is also capable of above thing
# from collections import OrderedDict
# ordered_dic=OrderedDict()
# ordered_dic['b']=6
# ordered_dic['c']=9
# ordered_dic['a']=1
# print(ordered_dic)

# defaultdic is similer to dic but if we assces key which is not present than it return default value rather than Error
# from collections import defaultdict
# de_dic=defaultdict(int) # in bracket we give type of default value in case of int it it 0 int flaot 0.0
# de_dic['a']=1
# de_dic['b']=2
# print(de_dic['c']) # this give 0 rather than Error


# deque doubley ended queue
# from collections import deque
# dq=deque()
# dq.append(1)
# dq.append(2)
# dq.append(3)
# dq.appendleft(4)
# dq.appendleft(5)
# print(dq)
# dq.pop()
# print(dq)
# dq.popleft()
# print(dq)






