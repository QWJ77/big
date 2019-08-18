def test():
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")


g=test()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) 这里就会报错了，虽然可以把C打印出来
# g.close()

for i in g:
    print(i)#用for循环打印就不会报错可以打印出C
print("-"*30)
g=test()
for i in g: #生成器只能迭代一次，再用要重新生成
    print(i)