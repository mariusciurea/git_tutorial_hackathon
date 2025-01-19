"""Git tutorial"""

def add_numbers(number1, number2):
    return number1 + number2

def get_numbers_from_sentence(sentence: str) -> list[float]:
    nb = []
    for char in sentence:
        if char.isdecimal():
            nb.append(float(char))
    return nb


if __name__ == "__main__":
    my_sentence = "I am 33 years old!"
    numerical_values = get_numbers_from_sentence(my_sentence)
    print(numerical_values)