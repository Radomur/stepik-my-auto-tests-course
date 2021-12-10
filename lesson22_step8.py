import os 
import math
from selenium import webdriver
import time 
link = "http://suninjuly.github.io/file_input.html"
file_name = "text.txt"

try:
    browser = webdriver.Chrome()
    browser.get(link)    
#Заполняем форму
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk")
#Получаем адрес директории где расположен Питон   
    current_dir = os.path.abspath(os.path.dirname(__file__))   
#Получаем адрес самого файла   
    url_file = os.path.join(current_dir, file_name)
    print(url_file)
    element = browser.find_element_by_id("file")
    element.send_keys(url_file)
    print("Файл загружен")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


