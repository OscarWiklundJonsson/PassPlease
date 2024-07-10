# This file contains functions for creating usernames.
# The plan is to use these as part of the "temp-account" feature that will be implemented in the future. Soon(tm)

import random
import string


def generate_username():
    # Generate a random username
    username = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    username += ''.join(random.choices(string.digits, k=random.randint(1, 3)))
    return username


def generate_email(username):
    # Generate a random email address
    email = username + '@changethis.com' # This mail is not real, it's just a placeholder.
    # Preferably it will use a real domain.

    return email