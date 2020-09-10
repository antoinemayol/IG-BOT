import json,os
if not __name__ == "__main__":from Secret.cryptage import crypt_password

secret_file = str(os.path.dirname(os.path.abspath(__file__)))+'/secret.json'

def read_secret(username):
    with open(secret_file) as json_file:
        data = json.load(json_file)
        password_crypted=data[username]

        return password_crypted

def write_secret(username,password=""):

    password = crypt_password(password)

    with open(secret_file, "r") as json_file:
        data = json.load(json_file)
        with open(secret_file, "w") as json_file:
            data[username] = password
            json.dump(data, json_file)

def get_username_list():
    with open(secret_file, "r") as json_file:
        data = json.load(json_file)
        return list(data.keys())

if __name__ == "__main__":
    from cryptage import crypt_password
    write_secret("lol","")
    print(read_secret("lol"))