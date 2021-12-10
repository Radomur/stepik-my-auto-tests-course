from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Создаем свою функцию с переменной х
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_tag_name("button")  
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    #Обращаемся к функции
    y = calc(x) 
    print("X=",x) 
    print("Y=",y)


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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
