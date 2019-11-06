import pytest

from selenium.webdriver import Chrome

from pages.first import FirstPage
from pages.search_page import SearchPage



@pytest.fixture
def browser():
	driver = Chrome()
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
	

