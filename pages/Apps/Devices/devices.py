

from pages.common import driver
from pages.common import click_element_by_selector, click_element_by_text, hover_element

from selenium.webdriver.common.keys import Keys


def test_apps_devices():

    # click_element("button.MuiButtonBase-root-122")

    # click_element("li.MuiButtonBase-root-122")

    # hover_element("fuse-navbar")
    click_element_by_text("button", "Add New Device")
    driver.quit()
