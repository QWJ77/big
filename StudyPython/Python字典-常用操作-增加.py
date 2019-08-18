# dic[key]=value
d={"name":"sz","age":"18"}
print(d,type(d),id(d))
d["height"]=180
print(d,type(d),id(d))
# 可变类型，因为ID没变，改的还是之前对象