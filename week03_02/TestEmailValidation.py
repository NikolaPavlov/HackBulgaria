import re


def email_validator(email):
        EMAIL_REGEX = re.compile(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$")
        if not EMAIL_REGEX.match(email):
            return False
        else:
            return True

print(email_validator("gogo@goran.net"))