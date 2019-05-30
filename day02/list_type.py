#这就是一个列表的数据类型,list也叫数组
alist = ['呵呵',4,'哈哈哈',9,5,20]
#访问list
def list_sel():
#通过索引访问  顺序取值:从0开始数
    print(alist[0])
#访问倒数第三位  从-1开始数
    print(alist[-3])
#通过切片访问第二位  语法:前索引值:后索引值 取到后索引值的前一位
    print(alist[1:2])
#访问 从第五个开始到后面的所有
    print(alist[4:])
#不增值的话 从第一个开始取值
    print(alist[:6])

#删除list中的元素
def list_del():
#调用删除方法 不填参数 默认删除最后一位
    alist.pop()
    print(alist)
#调用删除方法 填写参数:索引值 删除指定元素 并把删除的元素返回回来 赋值给a
    a=alist.pop(3)
    print(alist)
    print(a)

#增加list中的元素
def list_add():
    blist = [1,2,3,'4']
#增加在末尾
    blist.append('5')
    print(blist)

    clist=[6,7,8]
#合并两个list中的元素
    blist.extend(clist)
    print(blist)
#把括号里的list当成一个元素与前面的合并
    # blist.append(clist)
    # print(blist)

def list_update():
    qlist = [1,2,3,4,5]
#更新列表中的元素,根据索引进行更新,值写在=后面就行了
    qlist[4]=500
    print(qlist)

def list_order_by():
    qlist = [1,2,3,4,5]
#从小到大排序
    qlist.sort()
    print(qlist)
#从大到小排序
    qlist.sort(reverse=True)
    print(qlist)

def list_distinct():
    vlist = [1,2,2,4,9,9,5]
#set(vlist):使用set方法对list进行去重,去重后不是list类型{},用list()方法将这个数据转换成list类型
    vlist=list(set(vlist))
    print(vlist)
#len():获取列表的长度,有几个元素 返回几个元素
    print(len(vlist))

def list_work():
    dlist = [1,3,5,7,9]
#访问索引2
    print(dlist[2])
#切片访问索引1到4
    print(dlist[1:5])
#删除索引3
    dlist.pop(3)
    print(dlist)
#增加两个元素
    # dlist.append(6)
    # dlist.append(8)
    tlist = [6,8]
    dlist.extend(tlist)
    print (dlist)
#第0位元素改成字符5
    dlist[0]=5
    print (dlist)
#获取索引长度
    print(len(dlist))


if __name__ == '__main__':
    #list_sel()
    #list_del()
    #list_add()
    #list_update()
    #list_order_by()
    #list_distinct()
    list_work()