from selenium import webdriver

driver_path = 'C:\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
url = 'https:\\www.google.com.tw'
driver.get(url)

