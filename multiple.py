class A:
    def __init__(self):
        print('Class A')
        super().__init__()

    def a(self):
            print('function a')
class B:
    def __init__(self):
        print('Class B')
        super().__init__()
    def b(self):
            print('function B')
class C(B,A):
    def __init__(self):
        #print('Class C')
        super(). __init__()
    def c(self):
            print('function C')
c = C()
c.a()


