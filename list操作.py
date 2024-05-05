# 构造一个list
mlist = ['张三', '里斯', '王五', '赵六', '徐七', '王八']
print(mlist)

# 添加一个元素至末尾
mlist.append('孙九')
print(mlist)

mlist.insert(3, '崔思')
print(mlist)

# 修改第二个元素
mlist[1] = '李四'
print(mlist)

# 删除倒数第二个元素
del mlist[len(mlist)-2]
print(mlist)

# pop 删除
print("----- pop 删除-----")
print(mlist)
mlist.pop()
print(mlist)
print(mlist.pop(2))
print(mlist)

# 列表拼接
nlist = ['hello', 'world', 'my', 'name', 'is', 'myk']
mlist.extend(nlist)
print(mlist)

# 遍历
for index, element in enumerate(mlist):
    print("index : %d "  % index + "   element :", element)




