import string,random

def random_string(level_cryptage,string2):
    string = ""
    for u in range(level_cryptage):string+=string2[random.randint(0,len(string2)-1)]
    return string

def create_key(crypt_char_size=3):
    random.seed(666)
    all_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+string.whitespace
    crypt_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    key = {}

    for char in all_chars:
        key[char]=random_string(crypt_char_size,crypt_chars)

    return key

def crypt_password(password):
    key = create_key()
    crypt_password = ""
    for char in password:
        crypt_password+=key[char]
    return crypt_password

if __name__ == "__main__":
    print(crypt_password("tinolebg"))