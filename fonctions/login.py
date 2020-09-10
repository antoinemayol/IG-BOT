from ID.get_login_informations import get_login
from time import sleep

def login(self,username,password,stay_connect = False,first_use = False,only_username_safe = False):

    if stay_connect:
        if first_use:pass#enregistrer NU + MDP
        if only_username_safe:pass#enregistrer MDP
    elif not stay_connect:
        if first_use:pass#enregistrer NU
        if not first_use and not only_username_safe:pass#effacer MDP

    url_get = False

    self.driver.get("https://www.instagram.com/accounts/login/")
    sleep(1)
    #Entrée des logins
    self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
    self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
    self.driver.find_element_by_xpath('//button[@type="submit"]').click()
    
    while not url_get:
        try:
            #Si login mauvais
            text_error = self.driver.find_element_by_xpath('//p[contains(text(), "' + "Le nom d’utilisateur entré n’appartient à aucun compte. Veuillez le vérifier et réessayer." + '")]')
            url_get = True
        except:
            try:
                #Si mdp mauvais
                text_error = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]')
                url_get = True
                print("Your password is wrong ! ;)")
            except:
                if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                    #Si login et mdp bon !
                    url_get = True
                    self.account_login,self.username_good,self.password_good = True,True,True
                    print("\nBonjour "+self.username+", vous êtes maintenant connécté !")
