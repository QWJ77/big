# 内建函数、三方函数、自定义函数
# 函数的使用标书就是使用文档，功能描述等
# 直接在函数最上面加'''  '''注释


def caculate(a,b=1):
    '''
    计算两个数据的和，差
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，可选，默认值1
    :return: 计算结果，元祖：（和，差）
    '''
    he=a+b
    cha=a-b
    return (he,cha)


#     自己写help文档
help(caculate)