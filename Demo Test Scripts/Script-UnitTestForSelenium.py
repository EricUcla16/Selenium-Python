import unittest
#import htmlTestRunner
from selenium import webdriver


class SeleniumUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before all the methods")

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE AFTER all methods")
        cls.driver.close()
        cls.driver.quit()

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_search(self):
        self.driver.set_page_load_timeout(100)
        self.driver.get("https://google.com")

        print(self.driver.title)

        self.assertEqual(self.driver.title, "Google")

        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").click()

        print(self.driver.title)

        self.assertEqual(self.driver.title, "Automation step by step - Google Search")
        print("Test completed")


if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/ericgarthoffner/PycharmProjects/SeleniumLearnings/Reports"))
    unittest.main()
