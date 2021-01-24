# Python program to check prime numbers between 1 to 10

def prime_number():
    for n in range(1, 11):
        if n > 0:
            for i in range(2, n):
                if n % i == 0:
                    print("Not a prime number", n)
                    break
            else:
                print("Yes, its a prime number", n)
        else:
            print("Not a prime number")


prime_number()
