import string
def encrypt(text):
    alphabet = string.ascii_lowercase
    new_word = ""
    for i in text:
        new_letter = alphabet.find(i) + 13
        if new_letter > 26:
            new_letter = new_letter - 26
        new_word = new_word + alphabet[new_letter]
    
    return new_word

print(encrypt("hello"))
