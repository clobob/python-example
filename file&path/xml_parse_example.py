# -*- coding: utf-8 -*-
import sys
import xml.dom.minidom

reload(sys)
# 通过sys模块的setdefaultencoding解决UnicodeDecodeError中文错误
sys.setdefaultencoding("UTF-8")

point_to_dom = xml.dom.minidom.parse('books.xml')
point_to_root = point_to_dom.documentElement

all_tags = point_to_root.getElementsByTagNameNS("*","*")

# 跟节点名
print point_to_root.tagName
# 根节点是否包含属性？
print "%s has any attributes? %s"%(point_to_root.tagName,point_to_root.hasAttributes())
# 根节点下包含多少个子节点， 其中子节点的子节点也算， 以此类推
print "amount of tags is: " + str(all_tags.length)
# 打印父节点
print "%s's parent node is: %s"%(point_to_root.tagName,point_to_root.parentNode) 

i = 0
for tag in all_tags:
    #打印所以节点的名字
    print " The %d tag is: %s"%(i,tag.tagName)
    i+=1