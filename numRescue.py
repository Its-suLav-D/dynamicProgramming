def numRescueBoats(people,limit):
    people.sort() 
    # 3,3,4,5
    i, j = 0 , len(people)-1
    ans = 0 
    while i <=j:
        ans+=1 
        if people[i] + people[j] <= limit: 
            i+=1 
        j-=1
    return ans 


numRescueBoats([3,5,3,4],5) # 3 boats(1,2) (2) (3)