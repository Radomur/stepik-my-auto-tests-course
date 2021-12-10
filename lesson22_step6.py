from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    

    #Создаем свою функцию с переменной х
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    #Обращаемся к функции
    y = calc(x) 
    print("X=",x) 
    print("Y=",y)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    click1 = browser.find_element_by_id("robotCheckbox")
    click1.click()

    # Скроллим страницу вниз
    button = browser.find_element_by_tag_name("button")    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    click2 = browser.find_element_by_id("robotsRule")
    click2.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
