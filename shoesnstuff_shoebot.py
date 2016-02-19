import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint


username = ''	 # Enter username
password = ''    	# Enter password

card_number = '' # Enter your card number NO SPACES
exp_month = ''   # Enter the month your card expires (TWO DIGITS ex: 01)
exp_year = ''	 # Enter the year your card expires (TWO DIGITS ex: 16)
cvc = ''		 # Enter your CVC number

shoesnstuff_url = 'http://www.footaction.com/'

def check_sizes(sizes):
	for size in sizes:
		button = size.find_element_by_tag_name('span')
		if 'US 9' in button.text:
			print 'Attempting to buy size 9/9.5...\n'

			checkout_available = click_size(size)
			if checkout_available:
				x = 1
				return x


		elif 'US 10' in button.text:
			print 'Attempting to buy size 10/10.5...\n'

			checkout_available = click_size(size)
			if checkout_available:
				x = 1
				return x

		elif 'US 11' in button.text:
			print 'Attempting to buy size 11/11.5...\n'

			checkout_available = click_size(size)
			if checkout_available:
				x = 1
				return x
	
	x = 0
	return x




def click_size(size):
	size.click()
	try:
		driver.find_element_by_class_name('selected')
		try:
			driver.find_element_by_id('add-to-cart').click()
			return True
		except:
			print 'Checkout button not available\n'
			return False
	except:
		print 'didnt'


x = 0
print '\nNavigating to website...\n'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.sneakersnstuff.com/en/authentication/login")
print 'Logging in...\n'
login_container = driver.find_element_by_id('authentication-login-form')
inputs = login_container.find_elements_by_tag_name('input')
inputs[1].send_keys(username) # Username
inputs[2].send_keys(password) # Password
inputs[3].click()
driver.get(shoesnstuff_url)

print 'Script ready to run...\n'
raw_input("##### Press Enter to continue... #####")
print '\nGetting rid of newsletter...\n'
driver.refresh()
print 'Beginning attempts to buy...\n'

while x is 0:

	try:
		'Gathering all sizes available...\n'
		sizes = driver.find_elements_by_class_name('available')
		x = check_sizes(sizes)
		if x is 1:
			print 'Navigating to cart...\n'
			driver.get('http://www.sneakersnstuff.com/en/cart/view')
			driver.find_element_by_id('process-order').click()

			# card number container
			print 'Entering your information...\n'
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
			print 'Finalizing, get ready...\n'
			driver.find_element_by_id('submit-button').click()
		else:
			print('Reloading page, trying again...\n')
			time.sleep(randint(1,2))
			driver.get(shoesnstuff_url)




	except Exception as e:
		print e


