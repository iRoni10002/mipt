import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')

    return parser

def cacl_fibonachi_digit(n):
    n = int(n)
    if n < 3:
        return 1
    else:
        x = y = 1
        for i in range(n-2):
            z = x + y
            x = y
            y = z
        return y


if __name__ == '__main__':
    parser = create_parser()
    n = parser.parse_args(sys.argv[1:]).n
    print(cacl_fibonachi_digit(n))
