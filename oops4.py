class student:
    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.math=marks3
    def avg(self):
        return(self.web+self.python+self.math)/3
        # def getmarks(self):
        #     return self.math
        # def setmarks(Self):
        #     self.math=marks
        @classmethod
        def classMethodExample(cls):
            returncls.numberofsunject

student1=student(5,4,3)
student2=student(7,8,8)
student3=student(1,2,3)
print(student1.avg())
print(student2.avg())
print(student3.avg())