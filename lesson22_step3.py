from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
link = "http://suninjuly.github.io/selects1.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    

    """#Создаем свою функцию с переменной х
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))"""

    #Выбираем значение чисел
    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    print("X=",x)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text) #выбираем и преобразовываем текст в число
    print("Y=",y)
    s = (x, y)
    summ1 = str(sum(s)) #Ищем сумму и преобразовываем число в текст
    print("Summ=",summ1)

    #Раскрываем выпадающий список
    browser.find_element_by_tag_name("select").click()
    
    #Кликаем (выдбираем) нужный пункт
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summ1)   

    """browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value=summ1]").click()
    print("Выбрали:",summ1)"""

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
