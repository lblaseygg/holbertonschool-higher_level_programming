def print_last_digit(number):
    # Take the absolute value to handle negative numbers
    last_digit = abs(number) % 10
    
    # Print the last digit
    print(last_digit, end='')
    
    # Return the last digit
    return last_digit
