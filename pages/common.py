import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

action = ActionChains(driver)


def click_element_by_selector(selector, clickAgain=False):
    element = driver.find_element_by_css_selector(selector)
    element.click()
    time.sleep(2)

    if clickAgain:
        element.click()
        time.sleep(2)


def hover_element(id):
    element = driver.find_element_by_id(id)
    action.move_to_element(element).perform()
    time.sleep(2)


def click_element_by_text(element, text):
    btn = driver.find_elements(By.XPATH, f'//{element}')
    btnNew = None
    for i in btn:
        if i.text == text:
            btn_new = i
            break
    btnNew.click()
    time.sleep(2)


def fill_in_input(name)
    element = driver.find_element_by_name(name)
    element.send_keys("")
