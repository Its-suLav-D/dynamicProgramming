
def find_min(i,j,k,look_up_table,count):
    temp=[] 
    min_dif = {} 

    temp.append(look_up_table[i])
    temp.append(look_up_table[j])
    temp.append(look_up_table[k]) 

    current = 0 
    next_item  =1 
    while current < len(temp)-1: 
        for value in temp[current]: 
            for value_item in temp[next_item]:
                diff = abs(value-value_item)
                if diff in min_dif:
                    min_dif[diff] +=1 
                else: 
                    min_dif[diff]= 1
        current+=1 
        next_item+=1 

    values = list(min_dif.values())

    if not 1 in values:
        count+=1 
    return count

def numberOfWays(roads): 
    adjacency_list = {}
    count = 0 
    for a, b in roads:
        if not a in adjacency_list:
            adjacency_list[a] = [] 
        if not b in adjacency_list:
            adjacency_list[b] = []
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    keys_list = list(adjacency_list.keys())

    for i in range(len(adjacency_list)):
        for j in range(i+1, len(adjacency_list)):
            for k in range(j+1,len(adjacency_list)): 
                find_min(keys_list[i], keys_list[j], keys_list[k],adjacency_list,count)

    print(count)

numberOfWays([[1,2],[2,5],[3,4],[4,5],[5,6],[7,6]])
# numberOfWays([[1,2],[2,3],[3,4],[4,5]])