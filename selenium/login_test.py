'''
Created on Feb 21, 2016

@author: User
'''


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
driver.get("http://www.google.com") 
driver.quit()


