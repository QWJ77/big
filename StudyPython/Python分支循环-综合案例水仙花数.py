# 水仙花数，十位三次方*各位三次方*百位三次方=它本身
# 准备一个3位数
'''
让用户输入数据
判断数据有效性（保证数值是3位数）
'''
while True:
    num=input("请输入3位数值：")
    num=int(num)
    if not 100<=num<=999:
        print("你输入的数据无效，直接退出程序")
        exit()



    # 判断是否是水仙花数
    '''
    分解百位、十位、各位
    '''
    bai=num//100
    shi=num % 100//10
    ge=num % 100 % 10
    result=(bai**3+shi**3+ge**3==num)
    # 打印结果
    if result:
        print('%d是水仙花数'%num)
    else:
        print('%d不是水仙花数' % num)