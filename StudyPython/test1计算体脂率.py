'''
输入：
身高、体重、年龄、性别
处理数据：
1、计算体脂率  BMI=体重（kg）/(身高*身高)（米）
体脂率=1.2*BMI+0.23*年龄-5.4-10.8*性别（男：1 女：0）
2、判定是否在正常范围内
正常范围：男15%~18%，女25%~28%
输出：
告诉用户是否正常
'''
height=float(input("请输入身高（m）:"))

weight=float(input("请输入体重（kg）:"))
age=int(input("请输入年龄:"))
sex=int(input("请输入性别:（男：1 女：0）"))

BMI=weight/(height*height)
TZL=1.2*BMI+0.23*age-5.4-10.8*sex

minNum=0.15+0.10*(1-sex)
maxNum=0.18+0.10*(1-sex)

result=minNum<TZL<maxNum

print("你的体脂率是%f" % TZL)
print("你的体脂率是否符合标准",result)