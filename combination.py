def findAllPrimeNumber(n, prime):
    prime[0] = prime[1] = False
    for x in range(2, n+1):
        prime[x] = True
    
    base = 2
    while base*base <= n :
        if prime[x] == True :
            multi = base * 2
            while multi <= n:
                prime[multi] = False
                multi += base
        base += 1

def primeCombination(n):
    prime = [0] * (n+1)
    findAllPrimeNumber(n, prime)

    temp = []
    for x in range(n+1):
        if prime[x]:
            temp.append(x)
    print(findsubset(temp, len(temp), n))

def findsubset(arr, length, sum): 
    prev = {}
    counter = 0
    r = 0
    for i in range(length):
        counter += arr[i]

        if counter == sum :
            r+=1

        if counter > sum :
            cek = counter - sum
            if cek in prev :
                r += prev.get(cek)  
        
        prev[counter] = 1
    return r


n = 4227
primeCombination(n)