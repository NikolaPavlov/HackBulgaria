import sys


def main():
    filename = sys.argv[1]
    opened_file = open(filename, 'r')
    print(opened_file.read())
    opened_file.close()


if __name__ == "__main__":
    main()
