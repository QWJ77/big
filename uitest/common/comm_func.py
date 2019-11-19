'''一些公共函数'''
import os
import datetime
import pytest

'''删除过期截图，expire设置过期天数'''
def delete_expire_screen(expire=3):
    screenlist = []
    for i in os.walk("../screen/"):
        '''产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】'''
        screenlist = i[2]
        '''遍历文件名'''
    for i in screenlist:
        screentime = i.split("_")[0] #2019
        if screentime != '':
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            now = datetime.datetime.strptime(now, '%Y-%m-%d')
            screentime = datetime.datetime.strptime(screentime, '%Y-%m-%d')
            path = "../screen/{}".format(i)
            if((now-screentime).days>expire):
                if os.path.exists(path):
                    os.remove(path)
                    print("该截图文件({})已被删除！".format(i))
                else:
                    print("该截图文件({})不存在！".format(i))
