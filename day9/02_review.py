class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.state = '生的'
        self.condiments = []
    def cook(self,time):
        if time < 0:
            return(f'报错！')
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.state = '生的'
            elif 3 <= self.cook_time < 7:
                self.state = '半生不熟'
            elif 7 <= self.cook_time < 12:
                self.state = '熟了'
            else:
                self.state = '焦了'
    def add_condiments(self,condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'地瓜烤的时间是:{self.cook_time} ,状态是: {self.state}, 添加的调料是: {self.condiments}'
    
dg = SweetPotato()
dg.cook(3)
dg.cook(6)
dg.add_condiments('辣椒')
print(dg)

