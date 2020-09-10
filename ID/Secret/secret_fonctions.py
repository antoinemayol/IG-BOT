import json,os

secret_file = str(os.path.dirname(os.path.abspath(__file__)))+'/secret.json'

def get_secret():
    with open(secret_file) as json_file:
        data = json.load(json_file)
        username,password=data['username'],data['password']

    return username,password

def write_secret(username,password):
    with open(secret_file) as json_file:
        data = {"username":username,"password":password}
        json.dump(data, json_file)

if __name__ == "__main__":
    write_secret("tino","lebgh")
    #print(get_secret())