f1=open('a.txt',mode='r')
f2=open('a1.txt',mode='w')
data=f1.read()
f2.write(data)
f1.close()  
f2.close()

with open('a1.txt') as f:
    print(f.read())
    print(f.closed)
print(f.close)

