def all_primes(num):
    primes = []
    if num > 1:
        for prm in range(2, num):
            for i in range(2 , prm):
                if prm % i == 0:
                    break
            else: 
                primes.append(prm)
        return primes
    
for prm in all_primes(100):
    num = 2**prm - 1
    for i in range(2 , num):
        if num % i == 0:
            print(f"2^{prm} - 1 = {num} is not prime")
            break
    else:
        print(f"2^{prm} - 1 = {num} is prime")
