#需求:根据配置信息使用闭包实现不同人的对话信息﹖
# 例如对话:张三:到北京了吗?李四:已经到了·放心吧·
# 外部函数接受姓名参数
def func_name(name):
    # 内部函数保存外部函数的参数，并且完成数据显示的组成
    def inner(msg):
        print(name+":"+msg)
    # 查询闭包地址
    print(id(inner))
    # 外部函数要返回内部函数
    return inner
# 创建tom的闭包实例
tom=func_name("tom")
# 创建jeery闭包实例

jeery=func_name("jeery")
# 如果执行tom闭包，因为已经保存了name的参数，那么以后输入的时候都是，tom:xxxx
tom("小帅哥，快来玩呀！")
jeery("打死都不去")
tom("我不吃你")
jeery("我信你个鬼哦")