# python3
# Find maximum value of pairwise product.


if __name__ == '__main__':
    # Get user input.
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    # Sort input numbers.
    new_numbers = sorted(input_numbers)

    # Calculate.
    result = new_numbers[input_n - 1] * new_numbers[input_n - 2]

    # Print result.
    print(result)
