from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    

    #Создаем свою функцию с переменной х
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    #Выбираем значение атрибута для нашей переменной х
    treasure_id = browser.find_element_by_id("treasure")
    x = treasure_id.get_attribute("valuex")
    print("X=",x)
    
    #Обращаемся к функции
    y = calc(x) 
    print("Y=",y)

    #Вставляем значение в поле на странице
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    click1 = browser.find_element_by_id("robotCheckbox")
    click1.click()

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
