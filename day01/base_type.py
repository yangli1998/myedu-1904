a = 5
# def: 声明方法的关键字 ;int_demo: 方法的名字; (): 下面写方法的内容
def yang_a():
    # 声明一个变量 =前面是变量名 aint, = 后面是变量值,int类型的5
    yang = 5

    # type(aint) : 获取 aint的数据类型(变量类型), print: 打印出他的类型
    print(type(yang))

# def: 声明方法的关键字 ;str_demo: 方法的名字; (): 下面写方法的内容
def yang_b():
    # 声明一个变量 =前面是变量名 astr, = 后面是变量值,str类型的5
    yang = '5'

    # type(astr) : 获取 astr的数据类型(变量类型), print: 打印出他的类型
    print(type(yang))


# 这是一个main方法,可以直接执行,main方法下面不能再有其他方法
if __name__ == '__main__':
    # 打印
    print('Hello World')

    # 方法的调用 : 写方法的名字就行,加上()
    yang_a()
    yang_b()

def test1():


    print('test1')

def test2():


    print('test2')

def test3():


    print('test3')

def float_demo():
    afloat = 1.1
    print(type(afloat))

def type_zhuanghuan():
    b = '123'
    print(type(b))
    b = int(b)
    print( type( b ) )

def type_zhuanghuan1():
    b = 123
    print(type(b))
    b = str(b)
    print( type( b ) )
def str_join():
    a = 123
    b = '哈哈哈'
    c = '呵呵呵'
    print(b+c)
    print(str(a)+b)
    print('%s,%s'%(a,b))
    print('%s,%s,%s'%(a,b,c))
def add(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    return num1 + num2

if __name__ == '__main__':
    test3()
    test1()
    test2()
    # float_demo
    # type_zhuanghuan()
    # type_zhuanghuan1()
    # str_join()
    b = add(5,30)
    print('___________')
    print(a)
    print(type(a))
    print(b)

