class Student: 
    def __init__(self): 
        self.__name = "Bhautik" 
        self.__marks = 85 
    def display(self): 
        print("Student Name:", self.__name) 
        print("Student Marks:", self.__marks) 
        
# Create object
s = Student()

# Display data using method
s.display()