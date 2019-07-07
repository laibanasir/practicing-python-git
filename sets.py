#sets
integers = {1, 2, 3, 4, 5, 6, 6, 7} #repetitive elements will be considered once for eg 6 here
real = {7, 8, 9}
#sequence of unique elements

#discard
integers.discard(4)

#union
print(integers|real)

#intersection 
print(integers & real)

#difference (uncommon elements)
print(integers - real)
print(real - integers)

#symmetric difference (union of uncommon diefference) (xor operator , caret symbol ^)
print(integers ^ real)

#converting list into set
list_integers = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
set_integers = set(list_integers)
print(set_integers)
tuple_integers = tuple(list_integers)