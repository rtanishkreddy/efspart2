import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       #Pre-defined variables
       user = "instructor"
       pwd = "instructor1a"
       symbol = "test"
       name = "test"
       shares = "0"
       purchase_price = "0"


       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("https://efs-danial.herokuapp.com/admin/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Logged In"


       #Adding a new stock
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[3]/table/tbody/tr[3]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_xpath("//*[@id=\"id_customer\"]/option[2]")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_symbol")
       elem.send_keys(symbol)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name)
       elem = driver.find_element_by_id("id_shares")
       elem.send_keys(shares)
       elem = driver.find_element_by_id("id_purchase_price")
       elem.send_keys(purchase_price)
       elem = driver.find_element_by_xpath("//*[@id=\"stock_form\"]/div/div/input[1]")
       elem.click()
       time.sleep(2)
       driver.get("https://efs-danial.herokuapp.com/stock_list")
       time.sleep(3)
       assert "Posted New Test stock"


       #Deleting the last created stock
       driver.get("https://efs-danial.herokuapp.com/admin/portfolio/stock/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[1]/td[1]/input")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select/option[2]")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/button")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]")
       elem.click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("// *[ @ id = \"user-tools\"] / a[3]")
       elem.click()
       time.sleep(2)
       assert "Deleted New Test stock"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()