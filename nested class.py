class Developer:
    def __init__(self):
        self.d1='python'
        self.d2='java'
        self.d3=Tester()
    def disp(self):
        print('Developer1:', self.d1)
        print('Developer2:', self.d2)
class  Tester():
    def __init__(self):
        self.t1='automation'
        self.t2='manual'
    def show(self):
        print('Tester1:', self.t1)
        print('Tester2:', self.t2)         
dev=Developer()
# dev .disp()
print(dev.d3.show())

https://www.youtube.com/watch?v=AK9tUy5ZJQM