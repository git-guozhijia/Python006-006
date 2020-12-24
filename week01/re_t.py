import re
"""
telephone = "13122223333"
re.match 函数：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match(".{11}", telephone))
print(re.match(".{11}", telephone).group())
print(re.match(".{11}", telephone).span())
result = re.match(".{11}", telephone).group()
print(result)
email = re.match(".*@.*", "727988374@qq.com").group()
print(email)
print(re.match("(.*)@(.*)", "727988374@qq.com").group())
print(re.match("(.*)@(.*)", "727988374@qq.com").group(1))
print(re.match("(.*)@(.*)", "727988374@qq.com").group(2))
# 727988374@qq.com
# 727988374
# qq.com

# re.search()函数，查询整个字符串，查到匹配对象直接返回，返回结果就是第一个匹配到的字符
print(re.search("@","72798@8374@qq.com").group())# 返回查到的第一个字符，直接返回
# re.findall()函数，查询整个字符串，查到匹配对象直接返回，返回结果是所有的字符
print(re.findall("@","72798@8374@qq.com"))  # 返回字符串内匹配到的所有的字符

# re.sub()函数：替换操作
print(re.sub('@','&','72798@72798@qq.com'))
print(re.sub('\d','#','72798@72798@qq.com'))
print(re.sub('\d+','#','72798@72798@qq.com'))
# 72798&72798&qq.com
# #####@#####@qq.com
# #@#@qq.com

# re.split()函数：按照匹配的对象分割字符串，并返回一个字符串列表：如果想把匹配对象也分割开来，需要给这个字符加上()
print(re.split('@', '72798@72798@qq.com'))
print(re.split('(@)', '72798@72798@qq.com'))
# ['72798', '72798', 'qq.com']
# ['72798', '@', '72798', '@', 'qq.com']

#re.finditer()函数： 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
ii = re.finditer('(@)', '12312@dsfsdf@dsffwe2342@erwerwer')
for i in ii:
    print(i.group())
# @
# @
# @

# re.compile 函数：函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
"""

str_t1 = 'sda423ni555dn#ns3423ind#dsf34234nisdnn#342'

print(re.match(".", str_t1).group())
print(re.match(".*", str_t1).group())
print(re.match("s{1,33}", str_t1).group())
print(re.findall("s{1,33}", str_t1))



