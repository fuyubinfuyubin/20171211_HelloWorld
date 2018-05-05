1、输入输出：
	### Read user input ###
	age = input("How old are you?")
	height = input("How tall are you?")
	weight = input("How much do you weigh?")

	print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))

2、字符串输出：
	print('%s %s' % ('one', 'two'))
	print('{} {}'.format('one', 'two'))
	print('%d %d' % (1, 2))
	print('{} {}'.format(1, 2))

	print('{1} {0}'.format('one', 'two'))

	a = 5
	b = 10
	print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

3、list 序列
	#空list
	empty_list = []
	another_empty_list = list()

	#list
	weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']

	#替换list
	weekdays[0] = "Sunday"

	#删除list
	del weekdays[0]

	#移除
	weekdays.remove('Friday')

	#检验值是否在list中，输出true或false
	'Friday' in weekdays

	#append 加入 list中的值，
	weekdays.append('Friday')
	eg:
	{#code
	weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
	print(weekdays)
	weekdays.append('Monday')
	print(weekdays)
	#put
	['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday']
	}

	#list 相加
	weekend = ['Saturday', 'Sunday']
	weekdays = weekdays + weekend
	print(weekdays)

	#检索值得位置
	weekdays.index('Friday')

	#弹出pop
	last_day = weekdays.pop()
	print("last_day = ", last_day, "\nweekdays = ", weekdays)

	#list值排序
	nums = [1,4,2,5,3]
	sorted_nums = sorted(nums)
	print("nums =", nums, "\nsorted_nums =", sorted_nums)
	#output
	nums = [1, 4, 2, 5, 3] 
	sorted_nums = [1, 2, 3, 4, 5]

	#join 指定字符连接序列中元素后生成的新字符串
	  code：'-'.join('ABCDE')
	output：'A-B-C-D-E'

4、Tuple 元组
	#创建元组
	empty_tuple = ()   #空元组
	week_tuple = ('Monday', 'Tuesday')

	#元组赋值
	tom_tuple = ('Tom', 'Male', 20)
	name, gender, age = tom_tuple
	print("Name = ", name, "\nGender = ", gender, "\nAge = ", age)

	#互换值
	a = 1
	b = 2
	a, b = b, a
	print("a = ", a, "\nb = ", b)

5、Dictionary 字典
	#创建字典
	empty_dict = {}
	pizza = {
    "size":"medium", 
    "type":"pepperoni", 
    "crust":"Thick", 
    "qty": 1, 
    "deliver":True,
	}

	#输出
	pizza.keys()
	pizza.values()
	pizza.items()

	#插入一组key和值
	pizza['qty1'] = "2"

	#删除字典key和值
	del pizza['qty']  #[]中为key值

	#清空字典
	pizza.clear()

6、set 集合
	#创建set
	empty_set = set()
	even_set = {2,4,6,6,8,10} 

	#求交集
	even_set = {2,4,6,6,8,10}
	num_set = {3,6,9,12,15,18}
	num_set & even_set
	#output：
	{6} 

	#求并集
	num_set | even_set

	#转换为list
	list('ababc')

7、zip用法
	#zip ，zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
	s1 = 'abcdefg'
	s2 = 'hijklmn'
	list(zip(s1, s2))
	#output：
	[('a', 'h'),
	 ('b', 'i'),
	 ('c', 'j'),
	 ('d', 'k'),
	 ('e', 'l'),
	 ('f', 'm'),
	 ('g', 'n')]

	s1 = 'abcdefg'
	s2 = 'hijklmn'
	list((s1, s2))
	#output：
	['abcdefg', 'hijklmn']

8、
	s='hello'
	print("{} id is {}".format(s,id(s)))
	s='Yello'
	print("{} id is {}".format(s,id(s)))
	s= s+'w'
	print("{} id is {}".format(s,id(s)))



