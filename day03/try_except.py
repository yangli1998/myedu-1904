
if __name__ == '__main__':

# try  和 except 中间,写可能会出错的代码
# 如果出错 则执行except里面的代码
# 不出错 不会执行except里面的代码
# 不管出不出错 都不会影响其他代码的执行

    try:
        print('错误之前')
        a=5/0
        print('错误之后')
    except:
        print('报错了')

    print(1,2,3)
