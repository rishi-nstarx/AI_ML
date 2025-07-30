class Student:

    def __init__(self, name, roll_no, total_marks):
        self.name = name
        self.roll_no = roll_no
        self.__total_marks = total_marks

rishi = Student("Rishi", 21, 420)

print(dir(rishi))