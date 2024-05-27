class Student:
    school= "Akirachix"
    # age= 20
    # name="Amanda"
    # code= 39

    def __init__(self,name,age,code,):
                 self.name=name
                 self.age=age
                 self.code=code
    def __init__(self,first_name,last_name,age,code):
            self.first_name=first_name
            self.last_name=last_name
            self.age=age
            self.code=code
    def greet_student(self):
            greeting=f"Hello {self.first_name}, welcome to{self.school} your code is{self.code}"

    def year_of_birth(self):
            return f"{self.first_name} was born in {2024-self.age}"
    
    def student_full_name(self):
            return f"{self.first_name} {self.last_name}"
    
    def student_initials(self):
            return f"{self.first_name[0]} {self.last_name[0]}"
    


    