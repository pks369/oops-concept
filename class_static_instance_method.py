class A:
    surname='kumar'
    @classmethod
    def f1(cls,name):
        cls.n=name
        print(r'This is class method: {0}  {1}'.format(cls.n,cls.surname))
    @staticmethod
    def f2():
        print(f'static method')
    def __init__(self):
        print(f'instance class')
    def f3(self,address):
        self.a=address
        print('from {}'.format(self.a))

a=A()
a.f1('pappu')
a.f2()
a.f3('India')




class Mobile:
    fp='Yes'
    @classmethod
    def show(cls,r,c):
        x=cls.fp
        cls.ram=r
        cls.color=c
        print(r'Relame me fp:',x)
        print(r'Relame me ram:',cls.ram)
        print(r'Relame me ram:',cls.color)
a=Mobile()
Mobile.show('red','6')     