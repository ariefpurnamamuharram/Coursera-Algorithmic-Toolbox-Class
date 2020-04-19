# Python 3
# Fibonacci numbers.


def compute_fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]


if __name__ == '__main__':
    a = int(input())
    print(compute_fibonacci(a))
