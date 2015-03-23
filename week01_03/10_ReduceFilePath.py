import re

def reduce_file_path(path):
    answers = path.match("[\w]", path, flags=0)
    print(answers)

reduce_file_path("/protoss/coming.....here")