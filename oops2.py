class person:
 def __init__(self) :
   self.name="subham"
   self.age=18
   def updatename(self,name):
    self.name=name
    def compareage(self,other):
        if self.age == other.age:
            return True
        else:
            False

   
person1=person()
person2=person()
if person1.compareage(person2):
    print("they are of same age")
else:
    print("differennt age")