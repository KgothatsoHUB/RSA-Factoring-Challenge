#!/usr/bin/python3

import sys

def factorize(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            factor1, factor2 = factorize(number)
            if factor1 is not None and factor2 is not None:
                outfile.write(f"{number}={factor1}*{factor2}\n")
            else:
                outfile.write(f"{number} is a prime number\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output.txt"
    main(input_file, output_file)

