import re

telephone = "13122223333"

print(re.match(".{11}", telephone))

print(re.match(".{11}", telephone).group())
print(re.match(".{11}", telephone).span())

result = re.match(".{11}", telephone).group()
print(result)

email = re.match(".*@.*", "727988374@qq.com").group()
print(email)

print(re.match("(.*)@(.*)", "727988374@qq.com").group(1))
print(re.match("(.*)@(.*)", "727988374@qq.com").group(2))


print(re.search("@","72798@8374@qq.com").group())# 返回查到的第一个字符，直接返回
print(re.findall("@","72798@8374@qq.com"))  # 返回字符串内匹配到的所有的字符

print(re.sub('@','&','72798@72798@qq.com'))
print(re.sub('\d','#','72798@72798@qq.com'))
print(re.sub('\d+','#','72798@72798@qq.com'))

print(re.split('@', '72798@72798@qq.com'))
print(re.split('(@)', '72798@72798@qq.com'))