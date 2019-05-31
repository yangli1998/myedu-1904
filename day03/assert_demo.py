def assert_int():
    try:
        assert 2>1
        assert 3==3
        assert 1<2
    except:
        print('断言失败了')

def assert_str():
    a = '成功'
    b = '操作成功'
    try:
        assert a in b
        assert '成功'=='成功'
        assert a not in b
    except:
        print('断言失败了')


if __name__ == '__main__':
    assert_int()
    #assert_str()