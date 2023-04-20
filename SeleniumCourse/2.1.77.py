import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
x_treasure = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
x_element = x_treasure.get_attribute("valuex")
x = x_element
#calculate the result
y = calc(x)
#send answer to test
result = browser.find_element(By.ID, "answer")
result.send_keys(y)
#click robot ckeckbox
robotcheckbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
robotcheckbox.click()

robotradio = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
robotradio.click()

button = browser.find_element(By.CSS_SELECTOR, "[class ='btn btn-default']")
button.click()

# close browser
time.sleep(10)
browser.quit()