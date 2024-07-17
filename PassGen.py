import random
import string

special_chars = string.punctuation
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits


def generate_password():
    password = list(random.choice(special_chars)
                    + random.choice(uppercase_letters)
                    + random.choice(lowercase_letters)
                    + random.choice(numbers))
    all_chars = special_chars + uppercase_letters + lowercase_letters + numbers
    password += [random.choice(all_chars) for i in range(4)]
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print(generate_password())

