



factors = []


    
    
def find_factors(number):
    for i in range(1,number):
        for j in range(1,number):
            if(i*j==number):
                print(f"{i} {j}")
                if(i!=1 and j!=1):
                    listl = [i,j]
                    factors.append(listl)
                    print(listl)
                    find_factors(listl[1])
                    return
                    
                
                
                
find_factors(21)
primes = []
for i in range(len(factors)):    
    if(i==len(factors)-1):
        primes.append(factors[i][0])
        primes.append(factors[i][1])
        
    else:
        primes.append(factors[i][0])
        
print(max(primes))
    
# find_factors(20)
# find_factors(10)