#声明一个类 语法: class 类名(父类名)
class Human(object):
    #__init__ :类的初始化方法
    #self : 代表类的本身,name,age,sex 初始化的时候,要用到的参数
    def __init__(self,name,age,sex):
        #self.name = name : 把方法中的参数 绑定给类的属性
        self.name = name
        self.age = age
        self.sex = sex

    #类中的方法 必须包含self参数
    def eat(self):
        print(self.name+'在吃饭')

    def sleep(self):
        print(self.name+'在睡觉')
    #类中的方法,可以调用其他方法,可以调用属性,除了init方法
    def info(self):
        print('这个人叫%s,今年%s岁,性别:%s'%(self.name,self.age,self.sex))
        self.eat()

#继承 : 继承哪个类 就写哪个类
#继承之后 子类 拥有父类中的属性和方法
class Tester(Human):
    def __init__(self,name,age,sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job
     #如果子类中的方法名和父类中的重复了,那么这个叫重写方法,调用时调用子类中的方法
    def eat(self):
        print(self.name+'在吃工作餐')
    def do_test(self):
        print(self.name+'在做测试')
        self.sleep()
if __name__ == '__main__':
    #新建一个对象,根据Human类新建对象
    #对象是类的实例化
    # girl = Human('小葵',8,'女')
    #可以通过对象去调用类的方法和属性
    # girl.eat()
    # girl.sleep()
    # girl.info()
    # print(girl.sex)
    tester = Tester('小新',10,'男','测试')
    tester.do_test()
    tester.eat()
    print(tester.sex)
    print(tester.age)