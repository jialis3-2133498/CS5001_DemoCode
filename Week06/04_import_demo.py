import functions_params_return as fns


nums = [1, 2, 3, 4, 5]

doubled_nums = map(
    fns.double_num,
    nums
)

print(list(doubled_nums))


# def plus_5(x):
#     return x + 5


nums_plus_5 = map(
    lambda x: x + 5,
    nums
)


print(list(nums_plus_5))


primes = filter(
    fns.is_prime,
    [14, 2, 11, 15, 13, 16, 17, 12, 31, 10]
)

print(list(primes))


def is_not_prime(x):
    return not fns.is_prime(x)


non_primes = filter(
    is_not_prime,
    [14, 2, 11, 15, 13, 16, 17, 12, 31, 10]
)

print(list(non_primes))

non_primes = filter(
    lambda x: not fns.is_prime(x),
    [14, 2, 11, 15, 13, 16, 17, 12, 31, 10]
)

print(list(non_primes))
