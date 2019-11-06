import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
	driver = Chrome()
	driver.implicitly_wait(10)
	yield driver
	driver.quit()



def test_mapy_search(browser):
	URL = 'https://en.mapy.cz/zakladni?x=14.3999996&y=50.0499992&z=11'
	SEARCH = 'Dresden'

	browser.get(URL)

	search_input = browser.find_element_by_id('input-search')
	search_input.send_keys(SEARCH)
	search_input.send_keys(u'\ue007')

	WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/h1")))

	elem = browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/h1')

	assert elem.text == 'Dresden'
	

