
# 格式化输出
# name="sa"
# age=26
# print("我的名字是%s,我的年龄是%d" % (name, age))
# %[(name)][(flags)][(width)][(.precision)]typecode
# []:表示里面的内容可以省略
# （name）表示根据指定的名字，查找对应的值，格式化到字符串中
# mathScore=59
# englishScore=58
# print("我的英语分数是%(es)d，数学分数是%(ms)d"%({"es":englishScore,"ms":mathScore}))
# （width）表示占用的宽度
# print("%10d" %mathScore)
# （flags）表示对齐方式，默认右对齐，-表示左对齐，“ ”空格表示整数与负数对齐，0表示用0填充
# print("%-10d" %mathScore)
# print("% d" %mathScore)
# min=5
# sec=8
# 占2位。默认用空格填充，需要用0填充时加0
# print("%02d:%02d" % (min,sec))

# [.precision]表示小数点的精度

score=59.9
# print("%d" % score)取整数，59
# print("%f" % score)取6位小数
print("%.2f" % score)
# typecode必填