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
       category = "test"
       description = "test"
       acquiredvalue = "0"
       recentvalue = "0"


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


       #Adding a new Investment
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[3]/table/tbody/tr[2]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_xpath("//*[@id=\"id_customer\"]/option[2]")
       elem.click()
       elem = driver.find_element_by_id("id_category")
       elem.send_keys(category)
       elem = driver.find_element_by_id("id_description")
       elem.send_keys(description)
       elem = driver.find_element_by_id("id_acquired_value")
       elem.send_keys(acquiredvalue)
       elem = driver.find_element_by_id("id_recent_value")
       elem.send_keys(recentvalue)
       elem = driver.find_element_by_xpath("//*[@id=\"investment_form\"]/div/div/input[1]")
       elem.click()
       time.sleep(2)
       driver.get("https://efs-danial.herokuapp.com/investment_list")
       time.sleep(3)
       assert "Posted New Test Investment"


       #Deleting the last created Investment
       driver.get("https://efs-danial.herokuapp.com/admin/portfolio/investment/")
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
       assert "Deleted New Test Investment"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
