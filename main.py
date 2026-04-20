# 10-m
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f'{self.name} {self.subject} oqitadi')

t1 = Teacher("Ali", "Math")
t1.teach()
