def task_pair(arr):
    dp=[]
    weight=1
    for i in arr:
        for _ in range(i):
            dp.append(weight)
        weight+=1 
    result =[]
    for i in range(0,len(dp),2):
        temp=[]
        if i == len(dp)-1:
            break 
        for j in range(i, i+2):
            temp.append(dp[j]) 
        result.append(temp)
    return len(result)
                    



task_pair([6,5,3])