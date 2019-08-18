from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\LabUser\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.bing.com')

typing = browser.find_element_by_id('sb_form_q')

typing.send_keys('kim possible theme song')

typing.submit()

click = browser.find_element_by_class_name('inner')

click.click()

browser.close()
