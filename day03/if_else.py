def if_demo():
    #True为对
    a = 3>2
    #Flase为错
    # a = 3>4

    if a :
        print('a 是 True')
    else:
        print('a 是 Flase')

def elif_demo():
    a = 8
    # = 是 赋值,== 是 判断相等
    if a==1:
        print('a是1')
    elif a==2:
        print('a是2')
    elif a==3:
        print('a是3')
    elif a==4:
        print('a是')
    else:
        print('a不是1,2,3,4')



if __name__ == '__main__':
    #if_demo()
    elif_demo()