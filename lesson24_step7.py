import math
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    #Создаем свою функцию с переменной х
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))    

    browser = webdriver.Chrome()
    browser.get(link)    
    button = browser.find_element_by_id("book")
    
    #Ждем 19 сек. пока цена будет $100
    price = WebDriverWait(browser, 19).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))    
    print(price)

    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    #Обращаемся к функции
    y = calc(x) 

    input3 = browser.find_element_by_id("answer")
    input3.send_keys(y) 

    #Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    #Забираем число из модального окна
    alert = browser.switch_to.alert
    alert_text = alert.text
    t = alert_text.split(': ')[-1]
    print("keys =", t)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


