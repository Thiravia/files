#task1

#s = "this is My First Python programming class and i am learNING python string and its function"
#1 . Try to extract data from index one to index 300 with a jump of 3
#2. Try to reverse a string without using reverse function
#3. Try to split a string after conversion of entire string in uppercase
#4. try to convert the whole string into lower case
#5 . Try to capitalize the whole string
#6 . Write a diference between isalnum() and isalpha()
#7. Try to give an example of expand tab
#8 . Give an example of strip , lstrip and rstrip
#9.  Replace a string charecter by another charector by taking your own example
"sudhanshu"
#10 . Try  to give a defination of string center function with and exmple
#11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
#12 . Python is a interpreted of compiled language give a clear ans with your understanding
#13 . Try to write a usecase of python with your understanding .

s = "this is My First Python programming class and i am learNING python string and its function"

print(s[1:300:3])
print(s[::-1])
s1=(s.upper())
print(s1.split())
print(s1.lower())
print(s.capitalize())
#isalnum() which gives true if both alphapet and numbers are present
#isalpha() which gives true only when it contains alphapets are present
print(s.expandtabs())
print(s.rstrip())
print(s.replace('s','u'))
#python is compiler and interpretor first it will compile the data and then it will interpret

#task2
l = [1,2,3,4,5, "sudh" , 45.67, True]

print(l[5])
print(l[::1])
print(len(l))
print(l*2)
print(l+["suresh"])
print(l.append("suresh"))
print(l.reverse())

#task3
#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#1 . Try to reverse a list
#2. try to access 234 out of this list
#3 . try to access 456
#4 . Try to extract only a list collection form list l
#5 . Try to extract "sudh"
#6 . Try to list all the key in dict element avaible in list
#7 . Try to extract all the value element form dict available in list

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

print(l[::-1])
print(l[7][0])
print(l[5][1])
print(l[0:7])
print(l[8].keys())
print(l[8].values())

#task4

a,b,c,d=10,11,12,13
####### Question 01 #######
if a==10 or b==11 and c==12 and d==113: #### Case 1
    # this is equal to a==10 or (b==11 and c==12 and d==113)
    print('lets do something 1')
if (a==10 and b==11 ) or (c==12 and d==113):  #### Case 2
    # this is equal to (a==10 and b==11) or (c==12 and d==113)
    print('lets do something 2')
if a==10 and b==11 and c==12 and d==13 or a==9:   #### Case 3
    # this is equal to (a==10 and b==11 and c==12 and d==13) or a==9
    print('lets do something 3')
if a==9 or b==11 and c==12 and d==13:   #### Case 4
    print('lets do something 4')
############# Question 2 #########
# What is the difference between:
print(type(a) == int)
print(type(a) is int)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==10 or b==11 and c==12 and d==113:
    print("lets do something1")
if a==10 and b==11 or c==12 and d==113:
    print('lets do something 2')
if a==10 and b==11 and c==12 and d==13 or a==9:
    print('lets do something 3')
if a==9 or b==11 and c==12 and d==13:
    print('lets do something 4')

#type(a)==int and type(a) is int both will give the same result as true if the type of a is integer

#task 5
q1 :
ineruon
ineruon ineruon
ineruon ineruon ineruon
ineruon ineruon ineruon ineruon

q2 -

          ineruon
    ineruon      ineruon
ineruon		ineruon 	ineruon
	ineruon		 ineruon
		  ineruon

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

q3 : Try to extract all the list entity
q4 : Try to extract all the dict enteties
q5 : Try to extract all the tuples entities
q6 : Try to extract all the numerical data it may b a part of dict key and values
q7 : Try to give summation of all the numeric data
q8 : Try to filter out all the odd values out all numeric data which is a part of a list
q9 : Try to extract "ineruon" out of this data
q10 :Try to find out a number of occurances of all the data
q11 : Try to find out number of keys in dict element
q12 : Try to filter out all the string data
q13 : Try to Find  out alphanum in data
q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset
q15 : Try to unwrape all the collection inside collection and create a flat list

n=4
for i in range(n):
    for j in range(i+1):
        print("ineuron",end=" ")
    print()

n=3
for i in range(n):
    for j in range(n-i):
        print(" "*len('sudh'),end=" ")
    for j in range(i+1):
        print("ineuron",end=" ")
    print()
n=2
for i in range(n):
    for j in range(n+i):
        print(" " * len('  og'), end=" ")
    for j in range(n-i):
        print("ineuron",end=" ")
    print()

for i in l:
    if type(i)==list:
        print(i)

for i in l:
    if type(i)==dict:
        print(i)

for i in l:
    if type(i)==tuple:
        print(i)

for i in l:
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i:
            if type(j)==int:
                print(j)
for i in l:
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==int or type(v)==int:
                print(k)
                print(v)

l1=[1,2,3,4,2,3,4,5,6,3,4,5,6,7,45,4,5,23,3,6,7,8]

for i in l1:
    if i%2==0:
        pass
    else:
        print(i)

for i in l:
    if type(i)==list:
        for j in i:
            if j=="ineuron":
                print(j)

for i in set(l1):
    print(i,":",l1.count(i))

for i in l:
    if type(i)==dict:
        print(i)

for i in l:
    if type(i)==list:
        for j in i:
            if type(j)==str:
                print(j)
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==str or type(v)==str:
                print(k)
                print(v)

for i in l:
    m=1
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i:
            if type(j)==int:
                m = m *j
        print(type(i),":",m)
    if type(i)==dict:
        for k in i.items():
            for n in k:
                if type(n)==int:
                    m=m*n
        print(type(i), ":", m)

#task 6

a=1
b=9
while a<=b:
    print("*" *a)
    a = a + 1

a=1
b=1000
while a<=b:
    if a%2==0:
        print(a)
    a=a+1



