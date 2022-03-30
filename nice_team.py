def nice_team(arr,min_difference): 
    unique = set()

    pairs = 0 
    for i in range(len(arr)): 
        current_num = arr[i]
        if arr[i] not in unique:
            for j in range(0,i):
                if abs(current_num - arr[j]) == min_difference:
                    pairs+=1 
        unique.add(arr[i])
    
    return pairs 
    


# print(nice_team([3,4,5,2,1,1],3))

print(nice_team([1,1,1,1],1))