import json
import pytest

from selenium.webdriver import Chrome

from pages.first import FirstPage
from pages.search_page import SearchPage



@pytest.fixture(scope='session')
def config():
	with open('config.json') as config_file:
		data = json.load(config_file)
	return data	


@pytest.fixture
def browser(config):
	if config['browser'] == 'chrome':
		driver = Chrome()
	else:
		raise Exception(f'"{config["browser"]}" is not a supported browser')
	driver.implicitly_wait(10)
	yield driver
	driver.quit()



#try to add @pytest.mark.parametrize for check several search input

def test_mapy_search(browser):
	
	SEARCH = 'Dresden'

	

	search = FirstPage(browser)
	search.load()
	search.search(SEARCH)


	search_result = SearchPage(browser)
	assert search_result.search_result() == 'Dresden'
	

