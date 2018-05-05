
1、Lambda使用：Lambda是一个表达式，也可以说它是一个匿名函数。
然而在使用它或是阅读Lambda代码的时候，却显得并不那么容易。
因为它匿名，因为它删减了一些必要的说明信息（比如方法名）。
#使用函数
	def sum(a,b):
	    return a+b
	c = sum(2,3)
	print(c)
#使用lambda
	sum_lamnda = lambda m,n :m+n 
	g = sum_lamnda(3,4)
	print(g)

2、函数
	def zero():
	    print("You typed zero.\n")
	def sqr():
	    print("n is a perfect square\n")
	def even():
	    print("n is an even number\n")
	def prime():
	    print ("n is a prime number\n")
	options = {0 : zero,
	           1 : sqr,
	           4 : sqr,
	           9 : sqr,
	           2 : even,
	           3 : prime,
	           5 : prime,
	           7 : prime,}

	options[0]()

3、