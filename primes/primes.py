def is_prime(num):
    if not isinstance(num, int) or num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def sum_of_primes(nums):
    return sum([x for x in nums if is_prime(x)])