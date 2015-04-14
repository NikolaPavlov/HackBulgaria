import sys


def main():
    text_from_all_files = []

    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        opened_file = open(filename, 'r')
        text_from_all_files.append(opened_file.read())
        text_from_all_files.append("====================")
        opened_file.close()

    print('\n'.join(text_from_all_files))


if __name__ == "__main__":
    main()
