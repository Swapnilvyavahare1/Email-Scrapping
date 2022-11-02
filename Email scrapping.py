from selenium import webdriver

chrome_driver = '/Users/DELL 2/Class_May_27_Weekday_Python/Projects/Project_2_Email_Scrapping/drivers/chromedriver'

driver=webdriver.Chrome(chrome_driver)
driver.get('https://www.google.com')
