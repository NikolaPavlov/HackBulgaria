import os, binascii


def generate_random_string():
    print(binascii.b2a_hex(os.urandom(15)))

generate_random_string()
