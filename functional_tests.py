from selenium import webdriver

browser = webdriver.Chrome('D:/Projects/JobTrackBoard/chromedriver.exe')
browser.get('localhost:8000')

assert 'Django' in browser.title