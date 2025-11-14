def prime(num):
    if num < 2:
        return False
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def find_pseudoprimes_base_2(limit):
    print(f"--- Finding pseudoprimes to base 2 up to {limit} ---")
    pseudoprimes_list = []
    for n in range(2, limit + 1):
        if not prime(n):
            if pow(2, n - 1, n) == 1:
                pseudoprimes_list.append(n)
                
    return pseudoprimes_list

if __name__ == "__main__":
    limit = 10000
    found_primes = find_pseudoprimes_base_2(limit)
    
    print(f"\nFound {len(found_primes)} pseudoprimes (base 2) up to {limit}:")
    
    for i, p in enumerate(found_primes):
        print(f"{p:6}", end="")
        if (i + 1) % 10 == 0:
            print()
    print() 


