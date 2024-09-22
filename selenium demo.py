from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


PATH = r"C:\Program Files (x86)\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)


driver.get("https://www.youtube.com/watch?v=b5jt2bhSeXs&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=2")
print(driver.title)


search = driver.find_element_by_name("s")
search.send_keys("abcd")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()


