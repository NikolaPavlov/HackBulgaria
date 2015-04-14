import re

def reduce_file_path(path):
    directories = path.split('/')
    answers = []

    # Add only directory names and ..
    for directory in directories:
        if directory == '':
            continue

        if directory == '.':
            continue

        answers.append(directory)
        if directory == "..":
            if len(answers) > 1:
                answers.pop()
                answers.pop()
            # If we can't go back with .. return /
            else:
                return '/'

    answers = '/'.join(answers)
    answers = '/' + answers
    return answers


if __name__ == "__main__":
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))
