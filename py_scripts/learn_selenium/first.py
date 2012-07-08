from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.common.exceptions import WebDriverException

from datetime import datetime, date, timedelta
import time

SITE_URL = 'http://localhost:8000'

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the site home page
driver.get(SITE_URL)
print 'Home page is working. '

link = driver.find_element_by_id('property-search')
link.click()

WebDriverWait(driver, 10).until(lambda driver : driver.current_url.endswith('property-search/'))
print 'Property search page is working. '

now = datetime.now()
next_year = now + timedelta(days=365)

date_input = driver.find_element_by_id('property_arrival_date')
date_input.send_keys(next_year.strftime('%d/%m/%Y'))

form = driver.find_element_by_id('filters')
form.submit()
print 'Successfully did a search. '

first_property = driver.find_element_by_class_name('property')
link = first_property.find_element_by_tag_name('a')
property_detail_url = link.get_attribute('href')
driver.get(property_detail_url)

def find_booking_link(driver):
    try:
        booking_link = driver.find_element_by_link_text("Book this property")
        return booking_link
    except WebDriverException, e:
        print e

booking_link = WebDriverWait(driver, 10).until(find_booking_link)

print 'Property detail page is working. '
booking_href = booking_link.get_attribute('href')
booking_url = '%s/?check_in=%s' % (booking_href, next_year.strftime('%d/%m/%Y'))

driver.get(booking_url)

WebDriverWait(driver, 10).until(lambda driver : driver.current_url == booking_url)
print 'Property booking page is working. '

names = ['number_of_nights', 'number_of_people', ]
for name in names:
    input_element = driver.find_element_by_name(name)
    input_element.clear()
    input_element.send_keys("1")

input_element.submit()
print 'View cart page is working. '

checkout_button = driver.find_elements_by_class_name('submitBtn')[-1]
checkout_button.click()
WebDriverWait(driver, 10).until(lambda driver : driver.current_url.endswith('/checkout/'))
print 'Checkout page is working. '

import pdb; pdb.set_trace()

names_and_values = [
    ('name', 'Selenium Test'),
    ('email', 'fruitschen@gmail.com'),
    ('telephone', '12345'),
    ('mobile_phone', '12345'),
    ('arrival_time', '10 AM'),
    ('hear_about_us', 'Test Case'),
]
for name, value in names_and_values:
    input_element = driver.find_element_by_name(name)
    if name == 'hear_about_us': #make it visible first.
        driver.execute_script('$("#id_hear_about_us").css("visibility", "visible").show()')
    input_element.clear()
    input_element.send_keys(value)

input_element = driver.find_element_by_name('tos')
input_element.click()

classes = ['guest_name_input', 'guest_email_input', ]

for class_name in classes:
    input_element = driver.find_element_by_class_name(class_name)
    input_element.clear()
    input_element.send_keys("fruitschen@gmail.com")

import pdb; pdb.set_trace()

paypal_button = driver.find_elements_by_name('submitButton')[0]
paypal_button.click()



driver.quit()
