from time import sleep
from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless = True
username = input("instagram account username>")
password = input("instgram account password>")
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)/chromedriver.exe", options=options)
driver.get("https://instagram.com")
sleep(5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
sleep(5)
driver.get("https://www.instagram.com/"+username+"/saved/")
sleep(5)
driver.find_element_by_class_name("_9AhH0").click()
sleep(4)
try:
    while True:
            sleep(2)
            driver.find_element_by_xpath("//span[@class=\"wmtNn\"]").click()
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
except:
    print("finnished")
    driver.quit()