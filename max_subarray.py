def max_sub_array_of_size(k, arr): 
    max_sum, window_sum = 0,0 
    window_start = 0 

    for windowend in range(len(arr)): 
        window_sum += arr[windowend]

        if windowend >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start+=1  
    return max_sum 
    
max_sub_array_of_size(3,[2,1,5,1,3,2])