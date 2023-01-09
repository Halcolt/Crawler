from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com")

txtUser = driver.find_element("email")
txtUser.send_keys("billtrinh19@gmail.com")

sleep(5)



#browser.close()

#https://www.youtube.com/watch?v=EawbYWaTP_k