from selenium import webdriver
#from selenium.webdriver import FirefoxOptions

#opts = FirefoxOptions()
#opts.add_argument("--headless")
#browser = webdriver.Firefox(options=opts)
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
