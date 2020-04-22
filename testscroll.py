from selenium import webdriver
from time import sleep

def init():
	driver = webdriver.Chrome('/usr/local/bin/chromedriver')
	driver.get('file:///home/rtauler/linkedin/test.html')
	#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	#test1 = driver.find_element_by_id('test1')
	driver.execute_script('document.getElementsByClassName("test1")[0].setAttribute("id", "test1")')

	driver.execute_script('document.getElementById("test1").scrollTo( 0, 500)')
	#driver.execute_script("test1.scrollTo( 0, 500);")
	sleep(10)

init()

