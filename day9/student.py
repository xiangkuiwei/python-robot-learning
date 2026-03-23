"""
该文件用于记录 学生类, 学生的属性信息为: 姓名, 性别, 年龄, 手机号, 描述信息.
"""

# 1.定义学生类
class Student:
    # 2 定义init魔法方法，初始化学生信息
    """
    参数:
        name: 姓名
        gender: 性别
        age: 年龄
        phone: 手机号
        desc: 描述信息
    """
    def __init__(self, name, gender, age, phone, desc):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    # 3 定义魔法方法str，打印学生信息
    def __str__(self):
        return f"姓名: {self.name}, 性别: {self.gender}, 年龄: {self.age}, 手机号: {self.phone}, 描述: {self.desc}" 
    
# 4. 测试
if __name__ == '__main__':
    # 创建学生对象
    s = Student('小王', '男', 18, '12345678901', '描述信息')
    # 打印学生信息
    print(s)
    
    
