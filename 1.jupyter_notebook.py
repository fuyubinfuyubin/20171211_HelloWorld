1、创建新的运行环境Python2.7:
conda create -n py27 python=2.7

2、激活新建的环境py27：
Win:  activate py27
Mac:  source activate py27

3、安装kernel： 
pip install ipykernel

4、通过ipkernel工具给jupyter notebook 加一个环境：
python -m ipykernel install --name py27

5、退出py27环境：
Win:  deactivate
Mac:  source deactivate

6、查看本机安装了多少个kernel
jupyter kernelspec list

7、安装graphviz
conda install graphviz 
pip install graphviz 

8、导入graphviz模块（打开jupyter notebook）
import graphviz

9、导入sklearn、pandas 模块
import sklearn.datasets as datasets
import pandas as pd
iris=datasets.load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
y=iris.target

10、Git使用：

本机建立repository: 在命令行中新建一个文件夹，进入文件夹后，使用git init进行初始化
mkdir newgame
cd newgame
git init
将改动提交到暂存去，然后再交到代码库
git add ./
git commit -m '第一次改动'

https://github.com/fuyubinfuyubin/TEST1.git