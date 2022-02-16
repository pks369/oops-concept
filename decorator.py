'''
Generator:
              retuen the sequence of value
              use yield statement to return  the value from function                
'''

'''
  take one function as argument ,parameter and return  one function
  @ to specific the decorator to apply another function.
'''


# def decor1(num):
#     def inner():
#         b=num()
#         mul=b*5
#         return mul
#     return inner 
def decor(num):   #1 4
    def inner():   # 5
        a=num()
        add=a+5
        return add 
    return inner   #6
@decor   #2      
def num(): #3     #7
    return 10
#num=decor(num)   
print(num())    #8 