from math import sqrt

def check_prime(number:int):
    count = 0
    for i in range(1, number+1):
        if number%i == 0:
            count+=1
    return count

def check_prime_sqrt(number:int):
    count = 0
    for i in range(1,int(sqrt(number)+1)):
        if number%i ==0:
            count+=1
            if (i!=(number/i)):
                count += 1
    return count

def devisor(lim):
    for i in range(lim+1):
        print(check_prime_sqrt(i))


#print(check_prime_sqrt(7))
# print(check_prime_sqrt(24))
# print(check_prime_sqrt(18))
# print(check_prime_sqrt(1800000000))

devisor(100)
