# String formatting -> https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        print(
            # Decimal, Octal, Hexadecimal, Binary
            str(i).rjust(width, ' '),
            oct(i)[2:].rjust(width, ' '),
            hex(i)[2:].upper().rjust(width, ' '),
            bin(i)[2:].rjust(width, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
