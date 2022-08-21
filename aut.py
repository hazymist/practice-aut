from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.bing.com')   #Using selenium to go from bing to Youtube

typing = browser.find_element_by_id('sb_form_q')  #This is referencing an HTML tag within the site.


typing.send_keys('kim possible theme song') #Simulating typing here, this line here is writing text on youtube search bar

typing.submit()

click = browser.find_element_by_class_name('inner')

click.click()

browser.close()
