import json,os

secret_file = str(os.path.dirname(os.path.abspath(__file__)))+'/secret.json'

def get_secret(username):
    with open(secret_file) as json_file:
        data = json.load(json_file)
        password=data[username]

        #password = uncrypt_password(password)

    return username,password

def write_secret(username,password):

    #password = crypt_password(password)

    with open(secret_file, "r") as json_file:
        data = json.load(json_file)
        with open(secret_file, "w") as json_file:
            data[username] = password
            print(data, "lol")
            json.dump(data, json_file)

if __name__ == "__main__":
    write_secret("tino","lebgh")
    print(get_secret("antoine"))