"""
该文件用于 完成学生管理系统的 具体业务的操作, 即: 增删改查, 保存学生信息等...
"""
from student import Student
import time

# 1.创建学生管理系统类
class StudentCMS:
    # 2.使用魔法方法init，初始化属性信息
    def __init__(self):
        # 创建一个空列表，用于保存学生信息
        self.stu_list = []

        """ self.stu_list = [
            Student('德桦', '男', 81, '111', '刻骨铭心'),
            Student('志奇', '男', 22, '222', '我不是紫琦'),
            Student('紫琦', '男', 66, '333', '有请志奇'),
            Student('冷哥', '男', 88, '444', '谁动了我的水冷'),
            Student('卷帘', '男', 52, '555', '谁动了我的大酱'),
          ] """
    
    # 3.定义函数，实现管理系统打印界面
    # 因为该函数没有使用self，所以可以把该函数定义为静态函数
    @staticmethod
    def show_view():
        print("-" * 50)
        print("欢迎使用学生管理系统")
        print("1. 添加学生信息")
        print("2. 删除学生信息")
        print("3. 修改学生信息")
        print("4. 查询单个学生信息")
        print("5. 显示所有学生信息")
        print("6. 保存学生信息")
        print("0. 退出系统")
        print("-" * 50)
    
    # 4.定义函数，实现添加学生信息功能
    def add_student(self):
        # 4.1 提示用户输入学生信息
        name = input("请输入学生姓名:")
        gender = input("请输入学生性别:")
        age = int(input("请输入学生年龄:"))
        phone = input("请输入学生手机号:")
        desc = input("请输入学生描述信息:")
        # 4.2 创建学生对象
        stu = Student(name, gender, age, phone, desc)
        # 4.3 添加学生信息到列表中
        self.stu_list.append(stu)
        # 4.4 提示用户添加成功
        print(f"添加 {name} 同学成功!\n")

    # 5.定义函数，实现删除学生信息功能      
    def del_student(self):
        # 5.1 提示用户输入要删除学生的姓名
        del_name = input("请输入要删除学生的姓名:")
        # 5.2 遍历列表找到要删除的学生
        for stu in self.stu_list:
            if stu.name == del_name:
                # 5.3 删除该学生信息
                self.stu_list.remove(stu)
                # 5.4 提示用户删除成功
                print(f"删除 {del_name} 同学成功!\n")
                break
            else:
                # 5.5 提示用户删除失败
                print(f"未找到 {del_name} 同学!\n")
                

    # 6.定义函数，实现修改学生信息功能
    def update_student(self):
        # 5.1 提示用户输入要修改学生的姓名
        upd_name = input("请输入要修改学生的姓名:")
        # 5.2 遍历列表找到要修改的学生
        for stu in self.stu_list:
            if stu.name == upd_name:
                # 5.3 修改该学生信息
                stu.gender = input("请输入学生性别:\n")
                stu.age = int(input("请输入学生年龄:\n"))
                stu.phone = input("请输入学生手机号:\n")
                stu.desc = input("请输入学生描述信息:\n")
                # 5.4 提示用户修改成功
                print(f"修改 {upd_name} 同学成功!\n")
                break
        else:
                # 5.5 提示用户修改失败
                print(f"未找到 {upd_name} 同学,请重新操作!\n")

    # 7.定义函数，实现查询单个学生信息功能
    def search_one_student(self):
        # 7.1 提示用户输入要查找学生的姓名
        search_name = input("请输入要查找学生的姓名:")
        # 7.2 遍历列表找到要查找的学生
        for stu in self.stu_list:
            if stu.name == search_name:
                # 7.3 打印该学生信息
                print(stu, end = '\n\n')
                break
        else:
            # 7.5 提示用户查找失败
            print(f"未找到 {search_name} 同学,请重新操作!\n")
    
    # 8.定义函数，实现显示所有学生信息功能
    def search_all_student(self):
        # 8.1 判断学生列表长度是否为0。若为0，则提醒用户请添加学生后再查询
        if len(self.stu_list) == 0:
            print("请添加学生后再查询!\n")
        else:
            # 8.2 遍历列表，查询该学号对应的学生信息
            for stu in self.stu_list:
                print (stu)
            print()  # 为了格式好看，加个换行。

    # 9.定义函数，实现保存学生信息功能
    def save_student(self):
        # 9.1 关联 学生信息文件.
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            # 9.2 把[学生对象，学生对象，学生对象] -> [字典，字典，字典]
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            # 9.3 把字典列表， 持久化到文件中
            dest_f.write(str(stu_dict)) # 把列表转换成字符串

    # 10.定义函数，实现加载学生信息功能
    def load_student(self):
        # 10.1
        try:   
        # 10.2 关联学生信息文件
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f: 
                # 10.3 一次性读取所有数据。
                stu_data = src_f.read()
                # 10.4 把上述字符串转换为列表
                stu_list = eval(stu_data)
                # 10.5 如果列表为空就赋予空列表
                if len(stu_list) == 0:
                    self.stu_list = []
                # 10.6 把stu_list(列表套字典)转成[学生对象，学生对象，学生对象]
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            # 10.7 走到这里，说明目的地文件不存在，创建即可
            with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
                pass
    # 11.定义函数，把上面所有业务跑通
    def start(self):
        # 11.1 加载学生信息
        self.load_student()
        # 11.2 死循环，不断的玩
        while True:
            # 11.3 为了效果更明显加入延迟(休眠)
            time.sleep(1)
            # 11.4 打印界面
            StudentCMS.show_view()
            # 11.5 提示用户录入要操作的编号, 并接收.
            input_num = input("请输入要操作的编号:")
            # 11.6 根据用户输入的编号，调用对应的功能
            if input_num == "1":
                # 添加学生信息
                # print("添加学生信息\n")
                self.add_student()
            elif input_num == "2":
                # print("删除学生信息\n")
                # 删除学生信息
                self.del_student()
            elif input_num == "3":
                #print("修改学生信息\n")
                # 修改学生信息
                self.update_student()
            elif input_num == "4":
                # print("查询单个学生信息\n")
                # 查询学生信息
                self.search_one_student()
            elif input_num == '5':
                # 查询所有学生信息
                # print('查询所有学生信息\n')
                self.search_all_student()
            elif input_num == '6':
                # 保存学生信息
                self.save_student()
                print('保存学生信息\n成功!')
            elif input_num == '0':
                # 退出系统, 做二次校验
                result = input("是否要退出系统(y/n) ->")
                if result.lower() == 'y':
                    self.save_student()
                    print('谢谢您的使用, 期待下次再会!\n')
                    break
            else:
                # 输入错误
                print("输入的编号有误，请重新输入")

# 12. 在main中测试.
if __name__ == '__main__':
    # 12.1 创建学生管理系统对象.
    cms = StudentCMS()
    # 12.2 调用学生管理系统对象的start()函数, 启动学生管理系统.
    cms.start()
            