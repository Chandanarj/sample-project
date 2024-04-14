def fibonacci(limit):
    fib_seq = [0, 1]  # Initialize Fibonacci sequence with first two numbers
    while fib_seq[-1] + fib_seq[-2] <= limit:  # Continue until next number exceeds the limit
        fib_seq.append(fib_seq[-1] + fib_seq[-2])  # Add next Fibonacci number to the sequence
    return fib_seq

limit = int(input("Enter the limit for Fibonacci sequence: "))

print("Fibonacci sequence up to", limit, "is:")
print(fibonacci(limit))

