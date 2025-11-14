def all_primes(num):
    primes = []
    if num < 0:
        return "There are no negative prime numbers"
    if num > 1:
        for prm in range(2, num + 1):
            for i in range(2 , prm):
                if prm % i == 0:
                    break
            else: 
                primes.append(prm)
        return primes

text = int(input("Please enter a number : "))
print(all_primes(text))

