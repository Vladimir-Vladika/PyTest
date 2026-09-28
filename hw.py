def count_vowels(letters):
    letters = letters.lower()
    vowels = ['а', 'и', 'ю', 'э', 'о', 'ы', 'ё', 'у', 'е', 'я']
    quantity = 0
    for letter in letters:
        if letter in vowels:
            quantity += 1
    return quantity