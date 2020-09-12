from time import sleep

def try_login(self,stay_connect=False,connection_type=0):

    if stay_connect:
        if connection_type==0:pass#enregistrer NU + MDP
        if connection_type==2:pass#enregistrer MDP
    elif not stay_connect:
        if connection_type==0:pass#enregistrer NU
        if connection_type==1:pass#effacer MDP

    self.driver.get("https://www.instagram.com/accounts/login/")
    sleep(1)
    #Entrée des logins
    self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
    self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
    self.driver.find_element_by_xpath('//button[@type="submit"]').click()
    
    url_get = False
    password_good,username_good = True,True

    while not url_get:
        try:
            text_error = self.driver.find_element_by_xpath('//p[contains(text(), "' + "Le nom d’utilisateur entré n’appartient à aucun compte. Veuillez le vérifier et réessayer." + '")]')
            username_good = False
            return password_good,username_good
        except:
            try:
                text_error = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]')
                password_good,username_good = False,False
                return password_good,username_good
            except:
                if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                    return password_good,username_good
                    
