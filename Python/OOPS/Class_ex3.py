#self : self is a keyword which is represent current class properties

class Student:
    def input(self,fname,subject):
        self.fname= fname
        self.subject = subject
        
    def display(self):
        print("name : ",self.fname) 
        print("subject : ",self.subject) 
        
        
obj = Student()
obj.input("Harsh","Mobile App Development")
obj.display()          