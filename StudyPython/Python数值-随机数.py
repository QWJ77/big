# 都隶属于random
import random
#random()  [0,1)范围内的随机小数
print(random.random())
# choice(seq)从 一个序列中随机玄炽一个数值
seq=[1,5,6,7,9]
print(random.choice(seq))
# uniform(x,y) [x,y]范围内的随机小数
print(random.uniform(1,9))
# randomint(x,y) [x,y]范围内的随机整数
print(random.randint(1,3))
# randrange(start,stop=None,step=1) 返回给定区间的随机整数[start,stop),step设置步长
print(random.randrange(1,4,2))