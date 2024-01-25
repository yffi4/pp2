def filter_prime(numbers):
    prime_list = []

    for num in numbers:
        isprime = True
        if num > 1:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    isprime = False
                    
            if isprime:
                prime_list.append(num)

    return prime_list


lst = list(map(int, input().split()))
primes = filter_prime(lst)
print(primes)




