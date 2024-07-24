def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence[:n]

def main():
    n = int(input("Enter the number of terms in the Fibonacci seraies: "))
    if n <= 0:
        print("enter a positive integer.")
    else:
        fib_sequence = generate_fibonacci(n)
        print(f"The first {n} terms of the Fibonacci sequence are:")
        for term in fib_sequence:
            print(term, end=' ')
        print()

if __name__ == "__main__":
    main()


