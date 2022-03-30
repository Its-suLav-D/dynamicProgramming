

class AncestralTree:
    def __init__(self,name):
        self.name = name 
        self.ancestor = None  

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor,descendantTwo) 
    if depthOne > depthTwo:
        return backTrackAncestralTree(descendantOne, descendantTwo, abs(depthOne - depthTwo)) 
    else:
        return backTrackAncestralTree(descendantTwo,descendantOne, abs(depthTwo-depthOne))

def getDescendantDepth(topAncestor,descendent):
    depth = 0 
    while descendent != topAncestor:
        depth +=1 
        descendent = descendent.ancestor 
    return depth 

def backTrackAncestralTree(lower,upper, diff):
    while diff > 0:
        lower = lower.ancestor
        diff -=1 
    while lower != upper:
        lower = lower.ancestor
        upper = upper.ancestor 

    return lower


