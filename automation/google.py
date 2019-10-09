from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = None

try:
    cpath = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(cpath)
    driver.get('https://google.com')
    
    search_element = driver.find_element_by_name('q')
    
    search_element.send_keys('blue heeler puppies')
    search_element.send_keys(Keys().RETURN)
    
    driver.save_screenshot('heelers.png')

finally:
    if driver is not None:
        driver.close()