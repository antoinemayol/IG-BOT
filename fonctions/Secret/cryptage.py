import string,random

def random_string(level_cryptage,string2):
    string = ""
    for u in range(level_cryptage):string+=string2[random.randint(0,len(string2)-1)]
    return string

def create_key(crypt_char_size=3):
    random.seed(666)
    all_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+string.whitespace
    crypt_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    key = []
    nb_string = len(all_chars)
    key = [[all_chars[i]] for i in range(nb_string)]
    for i in range(nb_string):key[i].append(random_string(crypt_char_size,crypt_chars))

    return key

def crypt_password(password,crypt_char_size=3):
    key = create_key(crypt_char_size)
    crypt_password = ""

    for i in range(len(password)):
        for s in key:
            if s[0]==password[i]:
                crypt_password+=s[1]

    return crypt_password

def uncrypt_password(crypt_password,crypt_char_size=3):
    key = create_key(crypt_char_size)
    password = ""
    nb_string = int(len(crypt_password)/crypt_char_size)

    for i in range(nb_string):
        for s in key:
            if s[1]==crypt_password[i*crypt_char_size:i*crypt_char_size+crypt_char_size]:password+=s[0]
        
    return password

if __name__ == "__main__":
    print(crypt_password("tinolebg"))
    print(uncrypt_password("dSYxKa4KUNi2gdcQaYewHFb9"))