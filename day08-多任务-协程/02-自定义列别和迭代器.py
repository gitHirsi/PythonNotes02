"""
@Author : Hirsi
@ Time :  2020/7/5
"""

"""
自定义的迭代器，遍历自定义的列表
MyList类
    1.初始化方法__init__()
    2.__iter__（）方法，对外提供迭代器
    3.addItem()方法，用来添加数据
    
MyIterator类
    1.初始化方法
    2.迭代器方法
    3.next()方法
"""


# 自定义MyList类
class MyList(object):
    def __init__(self):
        # 定义实例属性，保存数据
        self.datas = []

    def __iter__(self):
        mi = MyIterator(self.datas)
        return mi

    def addItem(self, name):
        # ***追加保存数据
        self.datas.append(name)


# 自定义MyIterator类
class MyIterator(object):
    def __init__(self, datas):
        # 定义实例属性，保存信息数据
        self.datas = datas

        # 定义实例，记录迭代器的位置(默认是0)
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        # 1.判断当前下标是否越界
        if self.current_index < len(self.datas):
            # 2.根据房前下标获得元素
            data = self.datas[self.current_index]
            # 3.下标位置+1
            self.current_index += 1
            # 4.返回下标对应的元素数据
            return data
        else:
            # 5.如果越界抛出抛出异常
            raise StopIteration('下标越界')


if __name__ == '__main__':
    # 创建自定义列表对象
    ml = MyList()
    ml.addItem('汉库克')
    ml.addItem('克洛克达尔')
    ml.addItem('佩罗娜')
    # print(ml.datas)

    # for循环获取
    for stu in ml:
        print('姓名:', stu)

    print('-' * 20)

    # 手动获得迭代器，在next(迭代器)获取数据
    i = iter(ml)
    data = next(i)
    print(data)

    data = next(i)
    print(data)

    data = next(i)
    print(data)

    # 超出下标获取，报错
    # data = next(i)
    # print(data)
