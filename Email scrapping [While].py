import numpy as np
import re
from selenium import webdriver

complete_list = [] 
letter = 'y'

while letter == 'y':
    website = input('Enter URL:')
    chrome_driver = '/Users/DELL 2/Class_May_27_Weekday_Python/Projects/Project_2_Email_Scrapping/drivers/chromedriver'
    driver=webdriver.Chrome(chrome_driver)
    driver.get(website)
    page_source = driver.page_source
    EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
    list_of_emails = []
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        list_of_emails.append(re_match.group())
    for i,email in enumerate(list_of_emails):
        print(f'{i+1}:{email}')
    complete_list = complete_list + list_of_emails
    letter=input('Enter letter "y" or "n":')

np.savetxt("Email_sheet.csv", 
       complete_list,
       delimiter =", ", 
       fmt ='% s')
