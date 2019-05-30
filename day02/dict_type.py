# import json
# # 字典以{  }包起来, : 前面是 key ,后面是 value ; 多个键值对用 , 分隔开
# adict = {'username':'admin',"password":"123456"}
#
# #字典是无序的,它没有索引,只能通过 key 去访问 value ,并且 key 不能重复
# def dict_sel():
#     print(adict['username'])
#
# #更新字典里的value
# def dict_update():
# #通过key 去 修改value
#     adict['username']='ysl'
#     print(adict)
#
# #删除字典里的键值对
# def dict_del():
#     adict.pop('username')
#     print(adict)
#
# #增加字典里的键值对
# def dict_add():
#     adict['age']=21
#     print(adict)
# #合并
#     bdict = {'list':[1,2,3],'tuple':(4,5)}
#     #合并方式一:将bdict添加进adict
#     adict.update(bdict)
#     print(adict)
#     #合并方式二:将adict和cdict合并,生成一个ddict
#     cdict = {"password":"666666","class":"1904"}
#     ddict = dict(adict,**cdict)
#     print(ddict)
#
# #字典和字符的转换
# def dict_zhuanhuan():
#     print(type(adict))
#     # json.dumps(adict) 字典 转换成 字符串 , ensure_ascii=False : 防止中文乱码
#     str_dict = json.dumps(adict,ensure_ascii=False)
#     print(str_dict)
#     print(type(str_dict))
#
#     dict_str = '{"username": "卡见风使舵", "password": "123456"}'
#     # json.loads(dict_str)  字符串 转换 成字典
#     json_loads = json.loads (dict_str)
#     print (type (json_loads))

#新建一个字典变量,里面有两个键值对
edict = {'username':'admin',"password":"123456"}
#通过key访问一个值
def home_work1():
    print(edict['username'])
#删除一个键值对
def home_work2():
    edict.pop('username')
    print(edict)
#添加一个键值对
def home_work3():
    edict['age']=21
    print(edict)
#更改任意一个值
def home_work4():
    edict['username']='yangli'
    print(edict)
#再新建一个字典,将两个合并
def home_work5():
    ndict = {"class":"1904"}
    edict.update(ndict)
    print(edict)

if __name__ == '__main__':
    # dict_sel()
    # dict_update()
    #dict_del()
    #dict_add()
    #dict_zhuanhuan()
    home_work1()
    home_work2()
    home_work3()
    home_work4()
    home_work5()