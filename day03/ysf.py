#运算符
def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)  #10/8:商1余2
    print(a % b)  #取余数

#比较符 完成后 会返回一个bool值,只有True 和 Flase
def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b) # == : 判断相等
    print(a <= b)
    print(a >= b)
    print(a != b) # 不等于

# 自增 , 自减
d=3
def deng(d):
    d+=1    #d=d+1 自增
    print(d)
    d-=1    #d=d-1 自减
    print(d)
    d*=3    #d=d*3
    print(d)
    d/=9    #d=d/9
    print(d)


if __name__ == '__main__':
    deng(d)