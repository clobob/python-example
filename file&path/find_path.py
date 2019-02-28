# -*- coding:UTF-8 -*-
from os import listdir
from os.path import isfile,isdir,join
# 解决中文编码神奇，别说我没告诉你
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
To find spec_path from currentDir
return path if found or False if not found
'''
def find_path(src_dir,spec_path):
    dirs=[src_dir]
    
    while dirs:
        current_dir = dirs.pop(0)
        for fn in listdir(current_dir):
            if fn == spec_path:
                return join(current_dir,spec_path)
            if fn != "temprepo" or fn != ".svn" or fn != ".git":
                path = join(current_dir,fn)
            if isfile(path):
                continue
            dirs.append(path)
    return None
    
if __name__ == "__main__":
    # decode 和 encode 因为在nodepad++控制台显示乱码才加的，在cmd下直接运行显示正常
    print find_path(u"E:\\迁移公司库",u"啊").decode('utf-8').encode('gbk')
    print find_path(u"E:\\workspace",u"啊")
    