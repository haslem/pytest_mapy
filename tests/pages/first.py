from selenium.webdriver.common.by import By



class FirstPage(object):

	URL = 'https://en.mapy.cz/zakladni?x=14.3999996&y=50.0499992&z=11'
	SEARCH_INPUT_LOC = (By.ID, 'input-search')

	"""docstring for FirstPage"""
	def __init__(self, browser):
		super(FirstPage, self).__init__()
		self.browser = browser

	def load(self):
		self.browser.get(self.URL)


	def search(self, search):
		search_input = self.browser.find_element(*self.SEARCH_INPUT_LOC)
		search_input.send_keys(search)
		search_input.send_keys(u'\ue007')			