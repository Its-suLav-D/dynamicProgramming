P = 131 
M = pow(10,9) + 7 

def hash_me(string): 
    total = 0 
    length= len(string)-1
    for char in range(len(string)):
        value = ord(string[char]) 
        total += value * pow(P,length)
        length-=1 
    return total % M 


def authEvents(events):
    password = None
    result =[]
    for element in events:
        if element[0] == 'setPassword':
            password = hash_me(element[1])

        else:
            if not password is None:
                value = authorize(password, element[1])
                result.append(value) 
    return result 


def authorize(original_password,new_password):
    x = abs(original_password- int(new_password))
    if original_password == int(new_password): 
        return 1 
    elif len(str(x)) == len(new_password):
        return 1 
    else:
        return 0 



    





# print(authEvents([['setPassword','000A'],['authorize','108738450'], ['authorize','108738449'],['authorize','244736787']]))

# print(authEvents([['setPassword','1'],['setPassword','2'], ['setPassword','3'],['authorize','49'],['authorize','50']]))

# print(authEvents([['setPassword','a'],['auhthorize','97'], ['auhthorize','12756'],['authorize','12804'],['authorize','12829'],['auhthorize','12772'],['auhthorize','12797'],['auhthorize','98']]))



print(authEvents([['setPassword','brnTP3'],['setPassword','bnFb'],['setPassword','HnKYaX'],['authorize','776923238'],['setPassword','f'],['authorize','84'], ['setPassword','eog'],['setPassword','wwmq6O'], ['authorize','251714951'], ['setPassword','NIQ0Wobtq']]))