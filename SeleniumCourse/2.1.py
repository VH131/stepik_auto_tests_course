import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
#calculate the result
y = calc(x)
#send answer to test
result = browser.find_element(By.ID, "answer")
result.send_keys(y)
#click robot ckeckbox
robotcheckbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
robotcheckbox.click()

robotradio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
robotradio.click()

button = browser.find_element(By.CSS_SELECTOR, "[class ='btn btn-default']")
button.click()

# close browser
time.sleep(10)
browser.quit()