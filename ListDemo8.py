#coding:utf-8

nameList = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

print('------------------删除之前的列表--------------------------')

for name in nameList:
    print(name)

print('------------------pop 删除之后的列表--------------------------')



#del:根据下标删除
#pop:删除最后一个元素
#remove:

nameList.pop()

for name in nameList:
    print(name)

del nameList[0]

print('------------------del 删除之后的列表--------------------------')

for name in nameList:
    print(name)

nameList.remove('指环王')
print('------------------remove 删除之后的列表--------------------------')

for name in nameList:
    print(name)


