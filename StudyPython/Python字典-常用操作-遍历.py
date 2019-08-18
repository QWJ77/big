# 先遍历所有的key,根据指定的key获取对应的值
d = {"name": "sz", "age": "18","adress":"上海"}
keys=d.keys() #虽然不是列表，但是可遍历对象
for key in keys:
    print(key)
    print(d[key])

# 直接遍历键值对
kvs=d.items()
# print(kvs)  dict_items([('name', 'sz'), ('age', '18'), ('adress', '上海')])
d["xxx"]="ooo" #当字典发生变化时，Dictionary view object也会随之变化
for k,v in kvs:
    print(k,v)
