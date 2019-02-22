from numpy import *
import operator

#创建数据集和标签
def creatDataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A',"A","B","B"]
    return group, labels

 # inX为用于分类的输入向量，dataSet为训练样本集， labels为标签，
    # k用于表示最近邻居的数目，使用欧氏距离计算两点间的距离
def classify0(inX,dataSet,labels,k):   #kNN算法

    #dataSet.shape[0]返回数组的行数，即数据集中有多少条数据
    dataSetSize = dataSet.shape[0]
    #计算距离
    #title（）在行列方向上重复inX，列方向1次，行方向dataSetSize次
    #矩阵相减
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #差值平方
    sqDiffMat = diffMat**2
    #sum（）行元素相加
    sqDistances = sqDiffMat.sum(axis=1)
    #开方
    distances = sqDistances**0.5
    #对距离排序，返回索引值
    sortedDistIndicies = distances.argsort()
    #选择距离最小的k个点
    #记录一个类别次数的字典
    classCount = {}
    print(classCount)
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]= classCount.get(voteIlabel,0)+1
        print(classCount.get(voteIlabel,0))
        print(classCount)
    #排序
    print(classCount.items())
    #sorted()与sort（）
    #operator.itemgetter(1) 按第一列进行排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    # 输出计算结果，测试
    return sortedClassCount[0][0]

group,labels = creatDataset()
print(classify0([0,0], group,labels,3))

