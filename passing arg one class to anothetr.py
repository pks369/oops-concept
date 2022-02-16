class Student:
    def __init__(self,n,r):
        self.name=n
        self.rollNo=r
    def show(self):
            print('Name:',self.name,'\n','Roll No:',self.rollNo)
class  User:
    @staticmethod
    def disp(stu):
        print('Name:',stu.name,'\n','Roll No:',stu.rollNo)
        stu.show()
stu=Student('Rahul',101)   
# stu.show()
User.disp(stu)        