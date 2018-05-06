1、numpy

	import numpy as np
	import pandas as pd
	#input
(1) array使用：
	t=(1,2,3)
	a=np.array(t,dtype= 'int')
	print(a)
	#output
	[1 2 3]

	#input
	t=(1,2,3)
	a=np.array(t,dtype= 'int')
	print(a)
	#output
	['1' '2' '3']

	#input
	list1 = [1,2,3]
	list2 = [4.2,5.1,6.3]
	b = np.array([list1,list2])
	print(b)
	print(type(b))
	b.shape
	#output
	[[ 1.   2.   3. ]
	 [ 4.2  5.1  6.3]]
	 <class 'numpy.ndarray'>
	Out[25]:
	(2, 3)

(2) Create Special Arrays
	#input
	np.zeros([2,2])
	#output
	array([[ 0.,  0.],
	       [ 0.,  0.]])

	#input
	np.ones([2,2])
	#output
	array([[ 1.,  1.,  1.],
	       [ 1.,  1.,  1.]])

	#input
	np.empty([2,3]) 
	#output
	array([[ 1. ,  2. ,  3. ],
    	   [ 4.2,  5.1,  6.3]])

	#input
	np.eye(5)
	#output
	array([[ 1.,  0.,  0.,  0.,  0.],
	       [ 0.,  1.,  0.,  0.,  0.],
	       [ 0.,  0.,  1.,  0.,  0.],
	       [ 0.,  0.,  0.,  1.,  0.],
	       [ 0.,  0.,  0.,  0.,  1.]])

	#input 
	arange 从2开始，到10结束，步长为2
	np.arange(2,10,2)
	#output
	array([2, 4, 6, 8])

	#input
	0到10，平均分成4份
	np.linspace(0,10,4) # 3 numbers from 0 to 10
	#output
	array([ 0.        ,  3.33333333,  6.66666667, 10.        ])

（3）基本运算
a=np.array([[1,2,3,4],[5,6,7,8]])

相乘：a*a
幂运算：a**3
相加：a+a
相除：1/a
点乘：np.dot(a,b)  #a,b 为两个矩阵
相加：np.add(a,b)
