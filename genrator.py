def show():
    for i in range(1,101):
        yield i
        # print(type(i))
num=show()
for j in num:
    print(j,end =" ")