from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answ_element = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answ_element.send_keys(str(y))

    r_element = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    r_element.click()

    r_element = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    r_element.click()

    browser.find_element(By.CLASS_NAME, "btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла