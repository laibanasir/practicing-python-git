from functools import reduce

#learning lambda (anonymous functions) , filter
#even and odd filter

nums = [2, 5, 2, 1, 6, 7, 5, 20, 99, 102]
even_nums = list(filter(lambda n : n % 2 == 0, nums))
odd_nums = list(filter(lambda n : n % 2 != 0, nums))
print('Even numbers :', even_nums)
print('Odd numbers :', odd_nums)

#doubling odds and evens
#using map
#map replaces the values

even_nums_double = list(map(lambda n : n * 2, even_nums))
odd_nums_double = list(map(lambda n : n * 2, odd_nums))
print('Double even numbers :', even_nums_double)
print('Double odd numbers :', odd_nums_double)

#import reduce from functools to use reduce 

sum = reduce(lambda a, b : a + b, even_nums)
product = reduce(lambda a, b : a * b, odd_nums)
print('Sum of even numbers sequence :', sum)
print('Product of odd numbers sequence :', product)