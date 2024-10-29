# task 1

def quote():
    print('''"Don't compare yourself with anyone in this world...
if you do so, you are insulting yourself."''')

# quote()

# task 2

def show_numbers(start, end, predicate):
    for i in range(start, end):
        if predicate(i):
            print(i)

def is_even(a): 
    return a % 2 == 0

# show_numbers(2, 26, is_even)

# task 3

def print_square(side: int, symbol: str, fill: bool):
    filling_symbol = ' '
    if fill:
        filling_symbol = symbol
    print(symbol*side)
    for i in range (0, side -2):
        print(symbol + filling_symbol * (side -2) +  symbol)
    print(symbol*side)

# print_square(10, 'f', True)

# task 4

def find_minimum(*argv: float | int) -> float | int:
    for number in argv:
        for other_num in argv:
            if number > other_num:
                break
        else:
            return number
        
# print(find_minimum(56, 23, 55, 10, 5.5))

# task 5

def reduce_range(input_start: int, input_end: int, func) -> int:
    if  input_start > input_end:
        start = input_end
        end = input_start
    else:
        start = input_start
        end = input_end

    acc = start

    for i in range(start + 1, end + 1):
        acc = func(acc, i)
    return acc

def product(a, b):
    return a * b

# print(reduce_range(5, 8, product))

# task 6

def num_len(num):
    num = str(num)
    return len(num)

# print(num_len(1111111))

# task 7

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

# print(is_palindrome(421987))