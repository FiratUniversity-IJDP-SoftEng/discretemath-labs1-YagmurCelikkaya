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
            
def equation(n):
    return n**2 + n + 41

print("--- Testing n = 0 to 39 ---")
all_prime = True
for n in range(40): 
    value = equation(n)
    if prime(value):
        print(f"n = {n:2}, value = {value:4} -> Prime")
    else:
        print(f"n = {n:2}, value = {value:4} -> NOT PRIME")
        all_prime = False

if all_prime:
    print("\nSUCCESS: All values for n = 0 to 39 are prime.")
else:
    print("\nFAILURE: At least one value was not prime.")


print("\n--- Testing n = 40 ---")
n_40 = 40
value_40 = equation(n_40)

print(f"Calculating for n = {n_40}: {n_40}^2 + {n_40} + 41 = {value_40}")

if prime(value_40):
    print("Result: Prime")
else:
    print("Result: NOT PRIME")
    print(f"This is a composite number: 41 * 41 = {41 * 41}")

print("\n--- Testing n = 41 ---")
n_41 = 41
value_41 = equation(n_41)

print(f"Calculating for n = {n_41}: {n_41}^2 + {n_41} + 41 = {value_41}")

if prime(value_41):
    print("Result: Prime")
else:
    print("Result: NOT PRIME")
    print(f"This is a composite number: 41 * 43 = {41 * 43}")


