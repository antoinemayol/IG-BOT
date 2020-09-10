def start_driver(self):
    try:
        from selenium import webdriver
        self.driver = webdriver.Chrome()
    except ValueError:
        print("Something went wrong verify your driver files")

if __name__ =="__main__":
    start_driver(self)
    print("Done !")