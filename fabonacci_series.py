# Iterative Method
def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b10
    return series

# Recursive Method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_recursive(n):
    series = []
    for i in range(n):
        series.append(fibonacci_recursive(i))
    return series

# Generator Method
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Main program to call each method
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))

    print("\nFibonacci Series (Iterative):")
    print(fibonacci_iterative(n))

    print("\nFibonacci Series (Recursive):")
    print(generate_fibonacci_recursive(n))

    print("\nFibonacci Series (Generator):")
    print(list(fibonacci_generator(n)))
