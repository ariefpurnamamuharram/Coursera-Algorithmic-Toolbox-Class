# Python 3
# Least common multiple.
# ---
# a * b / gcd(a, b)


def greatest_common_divider(a, b):
    if a == 0:
        return b

    return greatest_common_divider(b % a, a)


def least_common_multiple(a, b):
    gcd = greatest_common_divider(a, b)

    return int(a * b / gcd)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(least_common_multiple(a, b))
