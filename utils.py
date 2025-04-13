import time

# Algorithms

def calculate_cube_root(number : float, epsilon : float = 0.01) -> dict:
    """
    Calculate the cube root of a given number.
    Using Bisection Method.
    
    Args:
        number (float): The number to calculate the cube root of.

    Returns:
        float: The cube root of the given number.
    """
    sign = -1 if number < 0 else 1 # Negative nums have -1 sign else +1
    low, high = 0, abs(number)
    
    guess = 0
    steps = 0

    start = time.time()  # Get time at start of loop

    while high - low > epsilon:
        guess = (low + high)/2  # Bisection method, hence picking guess at the centre

        if guess**3 < number:
            # When guess cube is less than our number 
            # Setting our new min/low to guess reducing our range to its half - guess to high
            low = guess
        elif guess**3 > number:
            # When guess cube is greater than our number
            # Setting our new max/high to guess reducing our range to its half - low to guess
            high = guess
        else:
            # If guess cube is equal to number, simply return guess as our cube root/ break loop
            break
        
        steps += 1
        
    end = time.time()  # Get time at end of loop
    return {'ans': guess*sign, 'steps': steps, 'time-taken': end - start}


def exhaustive_calculate_cube_root(num : float) -> dict:
    """
    Finds the cube root of numbers correct to 2 decimal places
    Exhaustive search method
    """
    i = 0
    steps = 1
    state = num
    num = abs(num)
    start = time.time()
    while i <= num:
        if i**3 > num:
            for j in range(10):
                if (i-1+j/10)**3 > num:
                    for k in range(10):
                        steps += 1
                        if (i-1+(j-1)/10 + k/100)**3 > num:
                            res = i-1+(j-1)/10 + (k-1)/100
                            if state < 0:
                                res = res*-1
                            end = time.time()
                            return {'ans': res, 'steps': steps, 'time-taken': end - start }
                else:
                    steps += 1
        else:
            steps += 1
        i += 1

def is_prime(number : int) -> str:
    if number % 2 == 0:
        # All even numbers are not prime
        return False
    for factors in range(3, int(number/2), 2):
        # Looping from 3 with a step of 2 to skip all even numbers - 0, 1 and 2 are not used in this space
        # No factors can be found from after half the number, so our search stops at number/2
        if number % factors == 0:
            # If a factor is found, the number is not prime
            return False    
    return True