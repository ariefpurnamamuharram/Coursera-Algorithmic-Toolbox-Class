# Python 3
# Greatest common divisor.


def greatest_common_divisor(a, b):
    if a == 0:
        return b

    return greatest_common_divisor(b%a, a)


if __name__ == '__main__':
    p, q = map(int, input().split())
    print(greatest_common_divisor(p, q))
