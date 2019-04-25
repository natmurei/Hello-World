class Student:
    def __init__(self,first_name,second_name,age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def fullname(self):
        name =self.first_name + self.second_name
        return name       
        
    def year_of_birth(self):
        return 2019-self.age

    def greeting (self):
        greet = "Hello {} {}, you were born in {}.".format(self.first_name,self.second_name,2019-self.age)
        return greet

    def initial(self):
        initial = self.first_name + self.second_name
        return initial






