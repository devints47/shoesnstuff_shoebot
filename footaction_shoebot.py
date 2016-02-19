import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint


cvc = ''		# Enter your CVC number
size = '10.0'	# Enter your size. Ex: 08.5, 09.0, 10.5, 12.5

footaction_url = 'http://www.footaction.com/product/model:254106/sku:BB5350/adidas-originals-yeezy-boost-350-mens/?cm=#sku=BB5350&size=' + size


x = 0
attempt_number = 1
print '\nNavigating to website...\n'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.footaction.com/")
raw_input('Log in and hit enter...\n')

print 'Navigating to shoe url...\n'
driver.get(footaction_url)
time.sleep(1)


while x is 0:
	try:
		print 'Attempting to add to cart #' + str(attempt_number) + '...\n'
		driver.find_element_by_id('addToCartLink').click()
		print 'Successfully added, navigating to checkout...\n'
		driver.get('http://www.footaction.com/shoppingcart/default.cfm?sku=')
		time.sleep(1)
		driver.refresh()
		driver.find_element_by_id('cart_checkout_button').click()
		print 'Entering CVV...\n'
		driver.find_element_by_id('payMethodPaneStoredCCCVV').send_keys(cvc)
		print 'Submitting order...\n'

		## Only uncomment the next line if you're ready to purchase
		# driver.find_element_by_id('orderSubmit').click()
		x = 1
	except Exception as e:
		print e
		attempt_number = attempt_number + 1
		print "Couldn't find the button. Refreshing...\n"
		driver.refresh()
