class Student:
    def __init__(self):
        self.current_weight = 100
    def run(self):
        print(f'疯狂跑步中...')
        self.current_weight -= 0.5
    def eat(self):
        print(f'疯狂进食中')
        self.current_weight += 2
    def __str__(self):
        return f'当前体重为:{self.current_weight}'

c1 = Student()
c1.run()
c1.run()
c1.eat()
print(c1)