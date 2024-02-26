# Exercise 1
from decimal import Decimal
import math

list_one = [1, 2, 3, 5, 4]
tuple_one = ('one', 'two', 'three')
float_one = 0.75
integer_one = 42
decimal_one = Decimal(0.42)
dictionary_one = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
}

# Exercise 2
round_up_float_one = math.ceil(float_one)

# Exercise 3
square_float_one = math.sqrt(float_one)

# Exercise 4
query_dictionary = dictionary_one['one']

# Exercise 5
query_tuple = tuple_one[1]

# Exercise 6
list_one.append(6)

# Exercise 7
list_one[0] = 0

# Exercise 8. The list contains numbers so instead of alphabetically is going to be ordered from lowest to highest
list_one.sort()

# Exercise 9
tuple_one += ('caramba',)