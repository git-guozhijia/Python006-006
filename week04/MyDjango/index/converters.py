class IntConverter:
	regex = '[0-9]+'

	def to_python(self, value):
		return int(value)

	def to_url(self, value):
		return str(value)


# 每个类除了类的名字是自定义的，方法名称和变量名称都是写死的固定格式
class FourDigitYearConverter:
	# 编写的正则表达式
	regex = '[0-9]{4}'

	def to_python(self, value):
		return int(value)

	def to_url(self, value):
		return '%d' % value
