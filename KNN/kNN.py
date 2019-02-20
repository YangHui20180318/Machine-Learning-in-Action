from numpy import *
import operator

#创建数据集和标签
def creatDataset():
    group1 = [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]
    print(group1)
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A',"A","B","B"]
    return group, labels

 # inX为用于分类的输入向量，dataSet为训练样本集， labels为标签，
    # k用于表示最近邻居的数目，使用欧氏距离计算两点间的距离
def classify0(inX,dataSet,labels,k):   #kNN算法
    print("dataSet:",dataSet)
    dataSetSize = dataSet.shape[0]
    print('dataSetSize:', dataSetSize)
    #计算距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print("diffMat:", diffMat)
    sqDiffMat = diffMat**2
    print("sqDiffMat:", sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    print("sqDistances:",sqDistances)
    distances = sqDistances**0.5
    print("distances:", distances)
    sortedDistIndicies = distances.argsort()
    print("sortedDistIndicies:", sortedDistIndicies)
    #选择距离最小的k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]= classCount.get(voteIlabel,0)+1

    #排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print("sortedClassCount:", sortedClassCount)
    return sortedClassCount[0][0]

group,labels = creatDataset()
print(classify0([0,0], group,labels,3))