# 指的是修改value
# dic[key]=value,如果key不在，则新增，在则修改
# d={"name":"sz","age":"18"}
# d["age"]=20
# print(d)


# 批量修改键值对
# oldDict=.update(newDic)
# 根据新的字典，批量更新旧字典的键值对
# 如果旧字典没有对应的key，则新增键值对
d={"name":"sz","age":"18"}
d.update({"age":"666","address":"上海"})
print(d)