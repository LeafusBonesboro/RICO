#import openpyxl
import xlwings as xw
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import time

#region Driver setup
from webdriver_manager.chrome import ChromeDriverManager
#learn to nest in divs. When accessing elements you access them by different properties. ID, class, name and other. These 3 are the most common. hierarchy is ID, name, and then class.
#Selenium returns the first element so the more unique the element tag is the more likely you are to get the element you want. 
options = Options()
options.add_argument("start-maximized:")
#endregion


#driver.get("http://www.google.com")
PATH = "C:\Program Files (x86)\chromedriver.exe"#change for laptop to chromedriver.exe path#driver = webdriver.Chrome(PATH) #this is the bad path file that gives error. this gives service object error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get("https://hvr-amazon.my.salesforce.com/00O4U000004SfTb/e?retURL=%2F00O%2Fo")#navigates here needs SSO, this actually goes to username/pw page also. Its dependant on something that tells int to go to SS or User/pw
driver.get("https://hvr-amazon.my.salesforce.com/00O4U000004SfTb/e?retURL=%2F00O%2Fo")
print(driver.title)

time.sleep(3)

search = driver.find_element(By.XPATH, '//*[@id="choose_idp"]')
search.click()
time.sleep(5)


#wk = xw.books.open(r'C:\Users\mbern\PycharmProjects\excelattempt\Dragondata.xlsx')
#sheet = wk.sheets("SheetA")

#df = sheet.range("M1:M10").options(pd.DataFrame).value

#xw.view(df)
#wk.close

#df = pd.read_excel(r'C:\Users\mbern\PycharmProjects\excelattempt\Dragondata.xlsx',engine="openpyxl") 

#results = df[df['contingency_type'].str.match('DrugTest')]
#print(results)

#book = openpyxl.load_workbook(r'C:\Users\mbern\PycharmProjects\excelattempt\Dragondata.xlsx')
#sheet = book["SheetA"]


#for row in sheet.iter_rows(min_row=1,max_row=5,min_col=3,max_col=6, values_only=True):

    #print(row)
