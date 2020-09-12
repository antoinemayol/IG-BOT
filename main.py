from time import sleep
from fonctions.login_console import login

class IG_BOT():
            
    def __init__(self):
        self.account_login = False
        
        self.start_driver()

        self.username, self.password ="",""
        login(self)
        '''
        A expliquer !
            verify files:
                - username_followers.txt
                - username_never_unfollow.txt
                - username_to_unfollow.txt
                (à voir soit on met des .txt ou des .json <- avantageant)
            get datas from files
            start prog and menu
        '''
        pass
        
    
    def start_driver(self):
        try:
            from selenium import webdriver
            self.driver = webdriver.Chrome()
        except ValueError:
            print("Something went wrong verify your driver files")

if __name__ == "__main__":IG_BOT()