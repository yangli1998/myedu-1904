def open_write1():
    #open(文件地址文件名,打开方式)
    #w+ : 写入时覆盖原有内容
    text_io = open('test.text','w+')
    for i in range(5):
        text_io.write('呵呵呵呵\n')

def open_write2():
    #a+ : 写入时追加内容
    text_io = open ('test.text','a+')
    for i in range (5):
        text_io.write ('嘻嘻嘻\n')

def open_read():
    text_io = open ('test.text','r')
    #读取所有行 返回一个list
    # print(text_io.readlines())
    #读取一行 字符串
    print(text_io.readline())


if __name__ == '__main__':
    # open_write1()
    # open_write2()
    open_read()