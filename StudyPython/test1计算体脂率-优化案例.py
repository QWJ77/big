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

# 容错处理
# 优先级not->and->or
# if 0<height<3 and 0<age<100 and 0<weight<150 and (sex==1 or sex==0):
if not (0<height<3 and 0<age<100 and 0<weight<150 and (sex==1 or sex==0)):
    print("数据不满足要求，程序退出")
    exit()

BMI=weight/(height*height)
TZL=1.2*BMI+0.23*age-5.4-10.8*sex
TZL/=100

# 区分男女
if sex==1:
    result = 0.15 < TZL < 0.18
elif sex==0:
    result = 0.25 < TZL < 0.28

# minNum=0.15+0.10*(1-sex)
# maxNum=0.18+0.10*(1-sex)
#
# result=minNum<TZL<maxNum

# print("你的体脂率是%f" % TZL)
# print("你的体脂率是否符合标准",result)

if sex==1:
    wenhao="先生你好"
    minNum=0.15
    maxNum=0.18
elif sex==0:
    wenhao="女士你好"
    minNum = 0.25
    maxNum = 0.28
if result:
    notice="恭喜你，身体健康，请继续保持"
else:
    if TZL>maxNum:
        notice="请注意，你的身体不正常，偏胖"
    else:
        notice="请注意，你的身体不正常，偏瘦"

print(wenhao,notice)