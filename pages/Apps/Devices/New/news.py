

from pages.common import driver
from pages.common import click_element_by_selector, click_element_by_text, hover_element

from selenium.webdriver.common.keys import Keys


def test_devices_new():
    hostName = driver.find_element_by_name("hostname")
    
    ipAddress = driver.find_element_by_name("address")

    llid = driver.find_element_by_name("site.llid")
    type = driver.find_element_by_name("site.type")
    bandWith = driver.find_element_by_name("site.bandwidth")
    core = driver.find_element_by_name("site.core")
    region = driver.find_element_by_name("site.region")
    domain = driver.find_element_by_name("site.domain")

    vendor = driver.find_element_by_name("device.vendor")
    model = driver.find_element_by_name("device.model")
    revision = driver.find_element_by_name("device.revision")
    memory = driver.find_element_by_name("device.memory")
    operatingSystem = driver.find_element_by_name("device.os")

    address =  driver.find_element_by_id("address")