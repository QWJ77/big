# 做一个简单的加法计算器，让用户输入两个值，输出对应结果
'''
要求：如果输错给提示并且从头输
数值超过100就报错
'''
while True:
     num1=float(input("请输入第一个数值"))
     num2=float(input("请输入第二个数值"))

     if num1>100 or num2>100:
          print("你输入的数据有问题，请重新输入")
          continue
     result=num1+num2
     print("你计算的结果是：",result)
     isQ=input("是否想退出（q:退出；其他：不退出，继续）")
     if isQ=='q':
          break