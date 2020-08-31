if not __name__ == "__main__": from ID.login_informations import username,password

def get_login(bot):
    #Ducplication des données d el'utilisateur
    username_to_send = username
    password_to_send = password

    instagram_password_minimum_size = 6
    password_too_small = True

    #Tant que nom d'utilisateur est vide
    while username_to_send == "" and not bot.username_good:

        #Aucune données n'est enregustré
        bot.log_not_save = True

        #Demande du nom d'utilisateur si non correct ou non existant
        if not bot.username_good : username_to_send=input("Enter your Instagram login:")

    #Tant que le mot de passe est trop petit
    while password_too_small:
        #Demande du mot de passe si non correct ou non existant
        if not bot.password_good : password_to_send=input("Enter your Instagram password:")
        #Si trop petit
        if len(password_to_send) < instagram_password_minimum_size:print("Your password is too small, it must be bigger than "+str(instagram_password_minimum_size)+".")
        #Si le mot de passe est asser grand passer à la suite
        elif len(password_to_send) >= instagram_password_minimum_size:password_too_small = False

    if bot.username != "": username_to_send = bot.username
    return username_to_send,password_to_send

#Débeugage
if __name__ == "__main__":
    print("Le débeugage ne marche pas ici")
