# del语句 删除指定元素(对象)
# 他不是方法
# nums=[1,2,3,4]
# del nums[1] #删除2
#
# nums2=666
# del nums2
# print('num2')

'''
pop 方法,删除并返回列表的默认最后一个元素
.pop(index=-1)
'''
# nums=[1,2,3,4]
# result=nums.pop()
# print(result)  #4
# result1=nums.pop(1)
# print(result1,nums) #2 [1, 3]

'''
移除列表中的某个元素
.remove(object),与pop区别在用pop参数填要删除的索引
从左往右删除 ,如果要删除的元素没有则报错
'''
nums=[1,2,2,2,3,4,2]
result=nums.remove(2)
print(result,nums)
'''
注意：不要在遍历内部移除元素，会造成混乱！
'''
# for num in nums:
#     print(num)
#     if num==2:
#         nums.remove(2)
# print(nums)