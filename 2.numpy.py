
1、定义矩阵、生成矩阵
C = np.array([[1,2,3],
            [1,1,1]])
D = np.array([[4,3,9,9],
            [1,1,2,2,],
            [4,2,1,1]]) 
2、查看数据类型
type(C)

3、查看矩阵形状
C.shape 

4、import sklearn 
from sklearn import datasets
from sklearn.metrics import auc
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso



