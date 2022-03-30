
def isPowerOfTwo(number): 
    s = math.log(number,2)
    return True if int(s) == s else False 

def bitwise_operation(arr):
    count = 0 
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            is_power = False 
            value = arr[i] & arr[j] 
            if value !=0:
                is_power = isPowerOfTwo(value) 
            if is_power: 
                count+=1 

    return count 


# [1,1,2,3]
print(bitwise_operation([0,2,4]))