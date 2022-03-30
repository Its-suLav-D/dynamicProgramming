def maxSumIncreasingSubsequence(array):
    sums = [num for num in array] 
    sequence = [None for _ in array] 

    maxSumIdx = 0

    for i in range(len(array)): 
        currentNum = array[i]
        for j in range(0,i):
            otherNum = array[j] 
            if otherNum  < currentNum and sums[j] + currentNum >= sums[i]: 
                sums[i] = sums[j] + currentNum 
                sequence[i] = j  
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i 

    return [sums[maxSumIdx],buildSequence(array,sequence,maxSumIdx)] 

def buildSequence(array, sequences, currentIdx):
    sequence = [] 
    while currentIdx is not None: 
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

print(maxSumIncreasingSubsequence([8,12,2,3,15,5,7])) # 8+ 12+15 = 35 