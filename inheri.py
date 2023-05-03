class Campus:
    stud_age = 22
    def __init__(self):
        self.age_1 = 22
    
    def fun_1(self):
        return 23 
    
class Secondary(Campus):
    high_age = 15
    def __init__(self):
        super().__init__()
        self.age_2 = 16

    def fun_2(self):
        return 17
    
class Primary(Secondary):
    pri_age = 6
    def __init__(self):
        super().__init__()
        self.age_3 = 7

    def fun_3(self):
        return 7

obj = Primary()

print(obj.stud_age, obj.age_1, obj.fun_1())
print(obj.high_age, obj.age_2, obj.fun_2())
print(obj.pri_age, obj.age_3, obj.fun_3())
