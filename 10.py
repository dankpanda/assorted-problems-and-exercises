import string

def pangram_check(text:str):
    alphabet = string.ascii_lowercase + " "
    alphabet_s = set(alphabet)
    if alphabet_s == set(text.lower()):
        return "It is a pangram"
    return "It is not a pangram"
print(pangram_check("The quick brown fox jumps over the lazy  dog"))