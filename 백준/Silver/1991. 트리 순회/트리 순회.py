import sys
# sys.stdin = open("input.txt", "r")

# Input
n = int(input())
root = "A"
myList = []
for i in range(n):
    myList.append(list(map(str, input().split())))

myList.sort(key=lambda x:x[0])

def getRoot(rootIdx):
    global myList
    return myList[rootIdx][0]

def getLeftChild(rootIdx):
    global myList
    return myList[rootIdx][1]
 
def getRightChild(rootIdx):
    global myList
    return myList[rootIdx][2]

def preOrderTraversal(rootIdx):
    root = getRoot((rootIdx))
    leftChild = getLeftChild((rootIdx))
    rightChild = getRightChild(rootIdx)
    leftChildIdx = ord(leftChild) - 65
    rightChildIdx = ord(rightChild) - 65

    print(root, end = "")
    if(leftChild != "."):
        preOrderTraversal(leftChildIdx)
    if(rightChild != "."):
        preOrderTraversal(rightChildIdx)

def inOrderTraversal(rootIdx):
    root = getRoot((rootIdx))
    leftChild = getLeftChild((rootIdx))
    rightChild = getRightChild(rootIdx)
    leftChildIdx = ord(leftChild) - 65
    rightChildIdx = ord(rightChild) - 65

    if(leftChild != "."):
        inOrderTraversal(leftChildIdx)
    print(root, end = "")
    if(rightChild != "."):
        inOrderTraversal(rightChildIdx)

def postOrderTraversal(rootIdx):
    root = getRoot((rootIdx))
    leftChild = getLeftChild((rootIdx))
    rightChild = getRightChild(rootIdx)
    leftChildIdx = ord(leftChild) - 65
    rightChildIdx = ord(rightChild) - 65
    
    if(leftChild != "."):
        postOrderTraversal(leftChildIdx)
    if(rightChild != "."):
        postOrderTraversal(rightChildIdx)
    print(root, end = "")

def solve():
    preOrderTraversal(0)
    print()
    inOrderTraversal(0)
    print()
    postOrderTraversal(0)
    print()

solve()
