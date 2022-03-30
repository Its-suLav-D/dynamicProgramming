def find_averages_of_subarray(K, arr): 
    result = [] 
    windowSum, windowStart = 0.0, 0  

    for windowEnd in range(len(arr)): 
        windowSum += arr[windowEnd]  
        # slide the window,
        if windowEnd >= K-1: 
            result.append(windowSum / K ) # Calcuate the average
            windowSum -= arr[windowStart] # Subtract the element going out 
            windowStart+=1 

    return result 


find_averages_of_subarray(5,[1,3,2,6,-1,4,1,8,2])
