from try_login import try_login
from Secret.secret_fonctions import get_username_list

def login(self=False):
    username_list = get_username_list()
    choice = 1
    if len(username_list)>1:
        while True:
            for i,user in enumerate(username_list):
                print(str(i+1)+" - "+user)
            choice=int(input("Quel compte ?"))
            if choice in range(1,len(username_list)+1):break

if __name__ == "__main__":
    login()