class student():

    def speak(self):
        print('%s 说我是一个%s岁的%s生' % (self.name,self.age,self.gender))


lipan=student()
lipan.name="帅哥"
lipan.age="15"
lipan.gender="男"
lipan.speak()
#>>>帅哥 说我是一个15岁的男生

#学习类（class）相关实践
#2020年2月18日15:16:19

class teacher():
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def introduce(self):
        print('%s是一名%s岁%sM高的老师' % (self.name,self.age,self.height))

Zhouxiaowu=teacher('傻逼','50','1.6')
Zhouxiaowu.introduce()
#>>>傻逼是一名50岁1.6M高的老师

#学习类class中init的应用，用于方便地自己对类的属性进行定义
#其中下划线开头的函数是声明该属性为私有，不能在类的外部被使用或访问
#2020年2月18日15:21:59

class boy(object):
    def __init__(self, n, a):
        # 设置属性
        self.name = n
        self.age = a

    # 输出一个字符串(追踪对象属性信息变化)
    def __str__(self):  # __str__(self)不可以添加参数(形参)
        return "名字：%s 年龄：%d" % (self.name, self.age)


# 实例化一个对象john
john = boy("约翰", 19)

# 当使用print输出对象时，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
print(john)
# >>>名字：约翰 年龄：19


class test():
    def __init__(self,n):
        self.name=n

    def say(self):
        print('名字是%s' % self.name)

    def __del__(self):
        print("实例%s已销毁"% self.name)

sb=test('sb')
sb.say()
print('---------------------')
del sb
sb.say()
#print()

#有关__del__的应用和用法试验