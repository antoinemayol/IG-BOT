from fonctions.try_login import try_login
from fonctions.secret.secret_fonctions import get_username_list,read_secret

def login(self=False):
    username_list = get_username_list()
    un_nb = len(username_list)
    connection_type = 0 # 0:new account, 1:safe account, 2;safe account without pw
    choice = 1
    while True:
        for i,user in enumerate(username_list):
            print(str(i+1)+" - "+user)
        print("________________\n"+str(un_nb+1)+" - New account")
        try:
            choice=int(input("\nQuel compte ?"))
            if choice in range(1,un_nb+2):break

        except:pass

    if choice != un_nb+1:
        self.username = username_list[choice-1]
        if read_secret(self.username) != "":
            connection_type = 1
            self.password = read_secret(self.username)
        elif read_secret(self.username) == "":connection_type = 2


    if connection_type != 1:
        if connection_type == 0:self.username = input("Entrez votre nom d'utilisateur :")
        self.password = input("Entrez votre mot de passe :")


    stay_connecte = input("Voulez rester connectez ?(O/N)")
    if stay_connecte == "O":stay_connecte=True
    else:stay_connecte=False
    try_login(self,stay_connecte,connection_type)

        

    

if __name__ == "__main__":
    login()