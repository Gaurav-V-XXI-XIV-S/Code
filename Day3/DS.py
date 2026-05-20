#__________________________________Time Complexity____________________________________________#
#find biggest number
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)

sampleArray = [5,7,9,2,3,4]
findBiggestNumber(sampleArray) #   O(1) +O(1) +O(1) +O(1) +O(N) = O(N)