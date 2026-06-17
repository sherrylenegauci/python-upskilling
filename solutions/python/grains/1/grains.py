def square(number):
    if (number > 64) or (number < 1):
        raise ValueError('square must be between 1 and 64')
    else:
         return 2 ** (number - 1)

def total():
    total = 0
    for i in range(1,65):
        number_of_grains = square(i)
        total += number_of_grains
    return total
        
        
