# 外层循环执行一次内层循环执行全部
# for i in range(1,6):
#     for j in range(1,3):
#         print(j)
# 案例：9*9乘法表
# 造一个集合

for num in range(1,10):
    for j in range(1,num+1):
        print("%d*%d=%d"%(j,num,j*num),end="\t")
    print("\n")

