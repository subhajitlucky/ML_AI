def factorial_for_loop(n):
   
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1): 
            result *= i
        return result


number = 5
print(f"The factorial of {number} is: {factorial_for_loop(number)}")

number = 0
print(f"The factorial of {number} is: {factorial_for_loop(number)}")

number = -3
print(f"The factorial of {number} is: {factorial_for_loop(number)}")