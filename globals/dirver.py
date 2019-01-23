from selenium import webdriver

class  Driver:
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(375, 812)