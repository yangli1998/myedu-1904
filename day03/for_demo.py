def for_demo1():
    #for(关键字) i(变量名,代表循环次数) in(关键字) range(迭代器函数)
    for i in range(6):
        print('hello world')
        print (i)   # 加上显示循环次数

def for_demo2():
    #两个参数时:从第一个参数开始计数,到第二个参数的前一位停止
    for i in range(4,9):
        print('hello world')
        print (i)

def for_demo3():
    #三个参数时:从第一个参数开始计数,到第二个参数的前一位停止  每次循环 递增 参数三(步长)
    for i in range(1,10,2):
        print('呵呵')
        print (i)

    #当步长为负数 : 第一个参数必须 > 第二个参数
    for i in range(12,3,-4):
        print('嘻嘻嘻')
        print (i)

#遍历 list
def for_list():

    alist = [9,5,4,9,1,7]
    # 方式一:
    for i in alist:
        print(i)

    blist = ['嘻嘻','呵呵','哈哈','嘿嘿','吼吼']
    # 方式二:
    for i in range(len(blist)):
        print(blist[i]) #如果print(i) 就会从0计数,有几个元素数几个为止

#嵌套循环
def for_for():
    for i in range(5):
        print('你好')
        for j in range(2):
            print('世界',end='!')     # end='  ' , 让print以引号内的内容结尾
        print('\n')   #\n : 换行   print默认: 以换行符结尾

def break_continue():
    for i in range(5):
        print(i)
        if i == 2:
            break    #终止所有循环

    for i in range(5):
        if i == 2:
            continue   #停止本次循环,直接开始下一次循环
        print(i)


if __name__ == '__main__':
    #for_demo3()
    #for_list()
    #for_for()
    break_continue()