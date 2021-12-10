from selenium import webdriver
import time
import datetime
link = "http://suninjuly.github.io/huge_form.html"
n=10

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name ("input")
    for element in elements:
        #n=n+1
        element.send_keys("User")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
