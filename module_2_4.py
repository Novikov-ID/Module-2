numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
print(len(numbers))
for i in numbers:
    if i == 1:
        continue
    elif i == 2 or i == 3:
        primes.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                not_primes.append(i)
                break
            else:
                is_prime = True
                primes.append(i)
                break
print('Primes:', primes)
print('Not Primes:', not_primes)
