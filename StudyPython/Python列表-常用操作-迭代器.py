'''
迭代是访问集合元素的一种方式，按照某种顺序逐个访问集合中的每一项
能够被迭代的对象被称为迭代对象
判断依据：能作用于for in
判定方法：
import collections
isinstance(obj,collections.Iterable) True:可迭代
'''
nums=[1,2,3]
import collections
result=isinstance(nums,collections.Iterable)
print(result)

#---------------------------迭代器---------------------------
'''
是可以记录遍历位置的对象
从第一个元素开始，往后通过next()函数进行遍历,可以自动记录当前的遍历位置
只能往后不能往前
判定依据：能作用与next()函数
判定方法：
import collections
instance(obj,collections.Iterator) True:可迭代对象
迭代器本身也是可迭代对象
迭代器适合巨大数列：因为在此之前，元素可以不存在，在此之后，元素可以被销毁。
因此它适合巨大和无限的数列，如：斐波那契数列（第三个元素是前两个元素的和）
它提供了一个统一的访问集合接口：iter（Iterator）
迭代器一般不能多次迭代
'''
result2=isinstance(nums,collections.Iterator)
print(result2)

# i=iter(nums)
# 生成迭代器

l=[1,2,3,4,5]
it=iter(l) #先根据列表生成迭代器，再用for...in...遍历迭代器
# next()
print(next(it))