'''
变量的作用域：变量的作用范围
Python是静态作用域
Python不存在
命名空间是作用域的体现形式
Python=LEGB
L-LOCAL函数内的命名空间
E-外部嵌套函数的命名空间，作用范围，闭包函数
G-GLOBAL-全局命名空间，作用范围当前模块
B-BUILTIN-内建函数命名空间，作用范围所有模块
'''

def test():
    a=1
