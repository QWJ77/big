# len()计算字符串的字符个数
# name="wo shi sz\n"  #转义符算是一个字符
# num=len(name)
# print(num)

#-----------------------对象方法------------------------------------
# find()查找子串索引（下标）位置,找不到返回-1
# find(self, sub, start=None, end=None，前开后闭
# name="wo shi sz\n"  #转义符算是一个字符
# num=name.find("sz")
# print(num)
# num1=name.find("s",3,7) #前开后闭

# rfind 从右往左查找，其他与find一样

# index，与find几乎一样，不同在于找不到该子串报错，类似于find是要查找，而index是去获取

# rindex同样的，从右往左

# count 计算某个子字符串出现次数
# name="wo shi sz"
# print(name.count("s"))

# replace 使用新字符串替换指定旧字符串
# replace(old.new[,count]) count代表要替换的个数
# name="wo shi sz"
# print(name.replace("s","z",1))
# print(name) #name本身是没变的，replace只是替换结果字符串！！！

# capitalize()  首字母大写，name本身是没变的！！！
# name="wo shi sz"
# print(name.capitalize())
# print(name)

# title 每一个单词的首字母大写，凡是不是字母的都可以当分隔符
name="wo shi-sz"
print(name.title())
print(name)

# lower 每一个字符均小写

# upper每一个字符均大写