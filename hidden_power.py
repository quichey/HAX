from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.youradress.org")#put here the adress of your page
elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
print(elem .get_attribute("class"))
driver.close()
"""
import urllib.request

with urllib.request.urlopen('http://webchal.hax.works:1234/') as response:
   html = response.read()

print(html)
"""
