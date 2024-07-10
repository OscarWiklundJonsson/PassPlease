import requests
import random
import string


def generate_password_word():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()

    # Select 4 random words
    selected_words = random.sample(words, 4)

    # Capitalize a random letter in each word
    password_parts = []
    for word in selected_words:
        word = word.decode('utf-8')  # Convert bytes to string
        index_to_capitalize = random.randint(0, len(word) - 1)
        capitalized_word = word[:index_to_capitalize] + word[index_to_capitalize].upper() + word[
                                                                                            index_to_capitalize + 1:]
        password_parts.append(capitalized_word)

    # Generate a random number
    random_number = str(random.randint(0, 99))

    # Form the final password
    password = ''.join(password_parts) + random_number
    return password


# Generate a random 4-digit PIN
def generate_pin():
    return ''.join(random.choices(string.digits, k=4))


# @todo: Implement this function
# This is a just a placeholder, this function will take a user-input as a K value and generate a random K-digit PIN.
def generate_strong_pin():
    return ''.join(random.choices(string.digits + string.ascii_letters, k=8))


# Generate a random 16-character PSK (Pre-Shared Key) for WPA2 or WPA3 security
def generate_psk():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
