# Create a class student 

class student : 
    def __init__(self):
        self.name = ''
        self.age = 0
        self.sciecne_marks = 0
        self.maths_marks = 0
        self.social_marks = 0

    def is_pass(self):
        avg = (self.maths_marks+self.social_marks+self.sciecne_marks)/3
        if avg >=40 :
            print('Pass')
        
        
   

ramesh = student()
ramesh.name = "Ramesh"
ramesh.age = 14
ramesh.maths_marks = 45
ramesh.social_marks = 76
ramesh.sciecne_marks = 89


suresh = student()
suresh.name = 'Suresh'
suresh.age = 14
suresh.maths_marks = 26
suresh.sciecne_marks = 38
suresh.social_marks = 70


raja = student()
raja.name = 'Rajavel'
raja.age = 14
raja.sciecne_marks = 87
raja.social_marks = 57
raja.maths_marks = 65


raja.is_pass()
suresh.is_pass()
ramesh.is_pass()

