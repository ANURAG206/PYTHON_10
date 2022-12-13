# class laptop:
#     def __init__(self):
#         self.name="asus"
#         self.processor="i9"
#     def printOutput(self):
#         print("my laptop name is:",self.name,"and the processor is:",self.processor )
class Person:
    def __init__(self,name,rollno) :
     self.name=name
     self.rollno=rollno
Person1=Person("anurag",19)
Person2=Person("atul",19)
print(Person1.name,id(Person1),Person1.rollno)
