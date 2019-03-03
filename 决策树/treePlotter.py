import matplotlib.pyplot as plt

#使用文本注解绘制树节点
decisionNode = dict(boxstyle = 'sawtooth',fc = '0.8')
leafNode = dict(boxstyle = 'round4',fc = '0.8')
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeText,centerPr,parentPt,nodeType):
    createPlot.axl.annotate(nodeText,xy = parentPt,xycoords = "axes fraction",xytext = centerPr,textcoords = 'axes fraction',va = "center",ha = 'center',bbox = nodeType,arrowprops = arrow_args)
#plotTree 函数
def plotMidText(cntrPt,parentPt,txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.axl.text(xMid,yMid,txtString)
def plotTree(myTree,parentPt,nodeTxt):
    numleafs  = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff +(1.0+float(numleafs))/2.0/plotTree.totalW,plotTree.yOff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if isinstance(secondDict[key],dict):    # 书上的type（secondDict[key]）._name_
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):

    fig = plt.figure(1,facecolor ="white")
    fig.clf()
    axprops = dict(xticks =[],yticks =[])
    createPlot.axl = plt.subplot(111,frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree,(0.5,1.0),'')

    plt.show()

#获取叶节点的数目和树的层次
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr1 = list(myTree.keys())
    #print(firstStr1)
    firstStr = firstStr1[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key],dict):
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs
def getTreeDepth(myTree):

    maxDepth = 0

    keyslist = list(myTree)
    firstStr = keyslist[0]

    secondDict = myTree[firstStr]

    for key in secondDict.keys():
        #print(type(secondDict[key])
        if isinstance(secondDict[key],dict):
            thisDepth  = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth>maxDepth : maxDepth = thisDepth
    return maxDepth
#测试以上部分
def retieveTree(i):
    listOfTree = [{'no surfacing': {0:'no',1:{"flippers":{0:"no",1:"yes"}}}},
                  {'no surfacing': {0: 'no', 1: {"flippers": {0:{'head':{0:"no", 1: "yes"}},1:'no'}}}}
                  ]
    return listOfTree[i]




myTree = retieveTree(0)
myTree['no surfacing'][3]='maybe'
print(getTreeDepth(myTree))
print(getNumLeafs(myTree))
#print(myTree)
createPlot(myTree)
