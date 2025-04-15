import time

def calculate_nth_root(number : float, n : int, epsilon : float = 0.01) -> dict:
    """
    Calculate the nth root of a given number.
    Using Bisection Method.
    
    Args:
        number (float): The number to calculate the nth root of.
        n(int): The n for nth root---

    Returns:
        float: The nth root of the given number.
    """
    sign = -1 if number < 0 else 1 # Negative nums have -1 sign else +1
    low, high = 0, abs(number)
    
    guess = 0
    steps = 0

    start = time.time()  # Get time at start of loop

    while high - low > epsilon:
        guess = (low + high)/2  # Bisection method, hence picking guess at the centre

        if guess**n < number:
            # When guess power n is less than our number 
            # Setting our new min/low to guess reducing our range to its half - guess to high
            low = guess
        elif guess**n > number:
            # When guess power n is greater than our number
            # Setting our new max/high to guess reducing our range to its half - low to guess
            high = guess
        else:
            # If guess power n is equal to number, simply return guess as our cube root/ break loop
            break
        
        steps += 1
        
    end = time.time()  # Get time at end of loop
    return {'ans': guess*sign, 'steps': steps, 'time-taken': end - start}

def euclidean_dist(point_1 : tuple, point_2 : tuple) -> float:
    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]
    # euclidean distance = sqrt((y1-y2)^2 + (x1-x2)^2)
    dist_squared = (y1 - y2)**2 + (x1 - x2)**2
    dist = calculate_nth_root(dist_squared, 2)['ans'] # Taking the square root
    return dist


# Testing this out, simply run this code
print("____________________________________")
print("Input points in format a, b like 1, 2")
point1 = [int(val) for val in input("Input your first point: ").split(',')]
point2 = [int(val) for val in input("Input your second point: ").split(',')]
print(euclidean_dist(point1, point2))