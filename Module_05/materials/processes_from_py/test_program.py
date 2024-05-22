import sys


def main():
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)


if __name__ == '__main__':
    main()