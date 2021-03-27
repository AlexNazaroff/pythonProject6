from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

binary = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
options = Options()
options.set_headless(headless=True)
options.binary = binary
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True #optional
driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")
driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()
