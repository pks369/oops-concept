class A:
    def __init__(self):
        print('class A')
    def a(self):
        print('function a')
class B(A):
    def __init__(self):
        print('class B')
    def b(self):
        print('function b')
class C(B):
    def __init__(self):
        print('class C')
    def c(self):
        print('function c')
c=C()
c.a()
c.b()
c.c()

