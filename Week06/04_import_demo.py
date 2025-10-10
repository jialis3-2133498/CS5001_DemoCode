import functions_params_return as fns

nums = [1, 2, 3, 4, 5]

double_nums = map(
    fns.double_num,  # we are not calling it, map do it
    nums
)

print(list(double_nums))

nums_plus_5 = map(
    lambda x: x + 5,  # We do not need a def plus_5(), we
    # can just use lambda function to do it
    nums
)
print(list(nums_plus_5))

prime = filter(  # filter takes function that returns true or false
    # and output a list of values that are true
    fns.is_prime,
    [14, 2, 11, 47, 13, 16, 17, 12, 31, 10]
)
print(list(prime))

non_primes = filter(
    lambda x: not fns.is_prime(x),
    [14, 2, 11, 47, 13, 16, 17, 12, 31, 10]
)
print(list(non_primes))
