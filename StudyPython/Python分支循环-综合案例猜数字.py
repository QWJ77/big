# 系统给一个数字，用户输入猜数字，如果不相等，继续要用户猜

num=500
count=0
while True:
    count+=1
    result=int(input("请输入结果："))

    if result==num:
        print("恭喜你，猜对了，答案就是:%d,你猜了%d次"%(result,count))
        break
    elif result>num:
        print("你输入的数字，太大了")
    else:
        print("你输入的数字，太小了")