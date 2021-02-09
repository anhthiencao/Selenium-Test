import time

from pages import login
from pages.Apps.Device import devices


def main():
    try:
        login.test_login()
    except NameError:
        print("Something went wrong")

    devices.test_apps_devices()


if __name__ == '__main__':
    main()

