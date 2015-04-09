import sys
from random import randint


def main():
    num_of_generated_nums = sys.argv[1]
    file_name = sys.argv[2]

    opened_file = open(file_name, 'w')
    for i in range(int(num_of_generated_nums)):
        opened_file.write(str(randint(1, 1000)) + ' ')
    opened_file.close()


if __name__ == "__main__":
    main()
