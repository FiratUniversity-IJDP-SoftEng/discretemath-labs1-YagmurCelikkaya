def prime(num):
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(f"{num} is an prime number")
        else:
            print(f"{num} is not an prime number")
    else:
        print(f"{num} is not an prime number")

text = int(input("Please enter an number : "))
prime(text)

