import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = ''	 # Enter username
password = ''    	# Enter password

card_number = '' # Enter your card number NO SPACES
exp_month = ''   # Enter the month your card expires (TWO DIGITS ex: 01)
exp_year = ''	 # Enter the year your card expires (TWO DIGITS ex: 16)
cvc = ''		 # Enter your CVC number

shoesnstuff_url = ''

def check_sizes(sizes):
	for size in sizes:
		button = size.find_element_by_tag_name('span')
		if 'US 10' in button.text:

			checkout_available = click_size(size)
			if checkout_available:
				x = 1
				return x
			else:
				x = 0
				return x




def click_size(size):
	size.click()
	try:
		driver.find_element_by_class_name('selected')
		print 'found selected'
		try:
			driver.find_element_by_id('add-to-cart').click()
			return True
		except:
			print 'button not available'
			return False
	except:
		print 'didnt'

x = 0
driver = webdriver.Firefox()
driver.get("http://www.sneakersnstuff.com/en/authentication/login")
login_container = driver.find_element_by_id('authentication-login-form')
inputs = login_container.find_elements_by_tag_name('input')
print inputs
inputs[1].send_keys(username) # Username
inputs[2].send_keys(password) # Password
inputs[3].click()
driver.get(shoesnstuff_url)


while x is 0:

	try:
		sizes = driver.find_elements_by_class_name('available')
		x = check_sizes(sizes)
		print x
		if x is 1:
			driver.get('http://www.sneakersnstuff.com/en/cart/view')
			driver.find_element_by_id('process-order').click()

			# card number container
			number_container = driver.find_element_by_class_name('card-no')
			number_container.find_element_by_tag_name('input').send_keys(card_number)

			# exp date container
			exp_date_container = driver.find_element_by_class_name('exp-dates')
			exp_date_container.find_element_by_tag_name('select').send_keys(exp_month)
			exp_date_container.find_element_by_id('expY').send_keys(exp_year)

			# cvc container
			cvc_container = driver.find_element_by_class_name('cvc')
			cvc_container.find_element_by_tag_name('input').send_keys(cvc)

			# Finalize Order page
			driver.find_element_by_id('submit-button').click()
		else:
			driver.get(shoesnstuff_url)
			time.sleep(1)




	except Exception as e:
		print e


