# Python 3
# Last Fibonacci digit.


def last_fibonacci_digit(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append((fibs[-1] + fibs[-2]) % 10)
    return fibs[n]


if __name__ == '__main__':
    a = int(input())
    print(last_fibonacci_digit(a))
