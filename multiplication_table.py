#!/usr/bin/env python3

def print_multiplication_table():
    """Prints a 9x9 multiplication table."""
    for i in range(1, 10):
        for j in range(1, i + 1):
            product = i * j
            # Use f-strings for clean formatting
            print(f"{j}x{i}={product}", end='\t')
        print() # New line after each row

if __name__ == "__main__":
    print_multiplication_table()