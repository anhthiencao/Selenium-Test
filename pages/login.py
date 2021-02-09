import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.common import driver
from pages.common import click_element_by_selector


def test_login():
    driver.get("http://192.168.1.74/login")

    nameInput = driver.find_element_by_name("username")
    passwordInput = driver.find_element_by_name("password")

    nameInput.send_keys("admin")
    passwordInput.send_keys("admin")
    time.sleep(2)

    click_element_by_selector("button[type='button']", True)

    click_element_by_selector("button[type='submit']")

    time.sleep(2)
