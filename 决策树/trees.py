from math import log
from numpy import *
import operator
from  treePlotter import *

#计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= float(prob * log2(prob))
    return shannonEnt

def creatDataSet():
    dataSet = [
        [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"]
    ]
    labels = ['no surfacing ','flappers']
    return dataSet, labels

#按照给定特征划分数据集
def splitDataSet(dataSet, axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方法
def chooseBestFeatureToSplit(dataSet):
    numberFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numberFeatures):
        featList = [example[i] for  example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in  uniqueVals:
            subDataSet = splitDataSet(dataSet ,i ,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy -newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#递归构建决策树
## 处理叶子节点中标签不唯一的情况，投票决定，返回出现次数的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] =0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteriems(), key= operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
## 创建树的函数代码
def creatTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0])== len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = creatTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree
#使用决策树执行分类
def classify(inputTree,featLabels,testVec):
    firstStr1 = list(inputTree.keys())
    firstStr = firstStr1[0]
    secondDict = inputTree[firstStr]

    featIndex=0
    if firstStr in featLabels:
        featIndex = featLabels.index(firstStr)

    for key in secondDict.keys():
        if testVec[featIndex] == key :
            if isinstance(secondDict[key],dict):
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel =secondDict[key]
    return classLabel
#使用pickle模块存储决策树
def stroeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

myDat,labels = creatDataSet()
print(labels)
myTree = retieveTree(0)
print(classify(myTree,labels,[1,0]))
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = creatTree(lenses,lensesLabels)
createPlot(lensesTree)