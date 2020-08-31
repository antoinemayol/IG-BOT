from ID.get_login_informations import get_login
from time import sleep

class IG_BOT():
            
    def __init__(self):
        self.account_login = False
        
        self.start_driver()

        self.username_good,self.password_good = False,False
        self.username, self.password ="",""
        while not self.account_login:
            self.log_not_save = False
            self.username, self.password = get_login(self)
            self.login()
        #verify files
        #get datas from files
        #start prog
        pass
    
    def start_driver(self):
        try:
            from selenium import webdriver
            self.driver = webdriver.Chrome()
        except ValueError:
            print("Something went wrong verify your driver files")
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(1)
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        url_get = False
        
        while not url_get:
            try:
                text_error = self.driver.find_element_by_xpath('//p[contains(text(), "' + "Le nom d’utilisateur entré n’appartient à aucun compte. Veuillez le vérifier et réessayer." + '")]')
                url_get = True
                print("Your username is wrong ! ;)")
            except:
                try:
                    text_error = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]')
                    url_get = True
                    print("Your password is wrong ! ;)")
                    self.username_good = True
                except:
                    if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                        url_get = True
                        self.account_login,self.username_good,self.password_good = True,True,True
                    
if __name__ == "__main__":IG_BOT()