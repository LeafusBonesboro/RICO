from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
options = Options().add_argument("start-maximized:")
#options.add_argument("start-maximized:")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.sample-videos.com/download-sample-csv.php")#(By.XPATH, '//*[@id="choose_idp"]')
driver.find_element_by_id("textbox").send_keys("tes")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link_to_download").click()

time.sleep(3)