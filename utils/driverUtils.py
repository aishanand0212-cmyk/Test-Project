from selenium import webdriver

def LaunchBrowser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def closebrowser(driver):
    driver.quit()