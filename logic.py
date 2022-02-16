'''
perfect square 
for i in range(1,101):
    if (i**(.5) == int(i**(.5))):
			   print(i, end=" ")
 '''
#https://www.w3resource.com/python
#for-loop
'''
iterating dict
color = {"c1":"Red", "c2": "Green", "c3": "Orange"}
for  key,value in color.items():
    print(key,value)
'''
'''
#count odd even no
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd=0
count_even=0
for i in numbers:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_even,count_odd)      
'''  

#while-loop 
'''
x = 0;
while (x < 5):
     print(x)
     x += 4
'''

'''
x = 0
s = 0
while (x < 10):
     s = s + x
     x +=1
else :
     print('The sum of first 9 integers : ',s)    
'''

'''
x = 1
s = 0
while (x < 10):
     s = s + x
     x = x + 1
     if (x == 9):
          break;
else :
     print('The sum of first 9 integers : ',s)        
print('The sum of ',x,' numbers is :',s) 
'''

'''
for x in range(7):
    if (x == 3 or x==6):
        break
    print(x)
'''

'''
a = "Python string"
b = a[4+3]
# print(b)

a = "Java"
b = "Script"
a+=b
#print(a)

a = "STRING"
i = 0
while i < len(a):
    c = a[i]
    print(c)
    i = i + 1
'''
''''
import collections
l=[1,1,23,45]
freqency=collections.Counter(l)
repeated={}
for key,value in freqency.items():
    if value>1:
        repeated[key]=value
print(repeated)
'''
'''
d = {0:10, 1:20}
d.update({2:30})
#print(d)

myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)
'''

'''
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

'''
'''
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print(color_dict[key])
'''

''''
import datetime
now=datetime.datetime.now()
today=datetime.datetime.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)


#print(now)
#print(today)
#print(yesterday)
print(yesterday)
'''

# file
# f1=open('a.txt','r')
# print(f1.read(5))
# print(f1.readlines())
# for read in f1:
#     print(read)
f2=open(' b.txt','a')
f2.write('nothing')
f2=open('b.txt','r')
# print(f2.read())
f2.close()

'''
import  os
if os.path.exists('c.txt'):
    os.remove('a.txt')
else:
    print('tt')
'''

# regular expression
##import re 
#s='This is Pappu and Soni from India'
#print(re.findall('Pappu'  'Soni',s))
#print(re.search('Pappu and Soni',s))
#print(re.sub('Pappu and Soni','Kishan and Gola',s))
# print(re.subn('India','Muzaffarpur',s))

'''
# os module
import os
for item in os.listdir():
    path=os.path.join(os.getcwd(),item)
    print(path)
'''

import sys 
# print(sys.argv)
x=int(sys.argv[3])
y=int(sys.argv[1])
add=x+y
print(r"total",add)


# def decor(num):
#     def inner():
# 	  add=a+15
# 	     return add
# 	inner()
# @decor()	  
# def num():
#    return 10
    
#A) The Python enumerate() function adds a counter to an iterable object. enumerate() function can accept sequential indexes starting from zero
'''
subjects = ('Python', 'Interview', 'Questions')
for k ,subject in enumerate(subjects):
   print(k,subject)
'''
#print(sum(range(1,11)))

#https://www.machinelearningplus.com/python/101-pandas-exercises-python/  pandas

#print(type(range(1,11)))

#pandas
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'Price': [np.NaN,15,5,5,10,15,15,5]
        }
df=pd.DataFrame(boxes)
# print(df)
#p=df.pivot_table(index='Color',values=['Price'],aggfunc='sum')
#c=df.loc[(df['Color']=='Green') &(df['Shape']=='Rectangle')]
#print(df.isnull().sum().any())
# df1=df['Price'].replace(np.NaN,10)
# print(df1)
# dpcp=df.copy()
# print(dpcp)
# sh_copy=df.copy(deep=False)
# print(sh_copy)

# df2=np.random.randint(1,11)
# print(df2)


# def show():
#     for i in range(1,101):
#         yield i
# value=show()
# for j in value:
#     print(j,end =" ")


'''
def show():
    for i in range(1,11):
        yield i
num=show()
for n in num:
    print(n,end=' ')
'''

# def sum_num(n):
#     count=0
#     for i in n: 
#         if i%2==0:       
#          count=count+i
#     print('sum of even',n,':',count,end='  ') 
#             else:
#                   print('sum of odd',n,':',count,end='  ') 
# sum_num(n=[2,3,5,4]) 

l=[2,3,5,6,8]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
         odd.append(i)
count=0 
for  e in even:
    count=count+e
print('Sum of the even element :',even,'=',count)

count1=0 
for  o in odd:
    count1=count1+o
print('Sum of the odd element :',odd,'=',count1)
    
   






