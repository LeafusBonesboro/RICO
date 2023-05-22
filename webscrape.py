#region imports

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
#endregion

#region Driver setup
from webdriver_manager.chrome import ChromeDriverManager
#learn to nest in divs. When accessing elements you access them by different properties. ID, class, name and other. These 3 are the most common. hierarchy is ID, name, and then class.
#Selenium returns the first element so the more unique the element tag is the more likely you are to get the element you want. 
options = Options()
options.add_argument("start-maximized:")
#endregion

#region
#driver.get("http://www.google.com")
PATH = "C:\Program Files (x86)\chromedriver.exe"#change for laptop to chromedriver.exe path#driver = webdriver.Chrome(PATH) #this is the bad path file that gives error. this gives service object error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get("https://hvr-amazon.my.salesforce.com/00O4U000004SfTb/e?retURL=%2F00O%2Fo")#navigates here needs SSO, this actually goes to username/pw page also. Its dependant on something that tells int to go to SS or User/pw
driver.get("https://hvr-amazon.my.salesforce.com/00O4U000004SfTb/e?retURL=%2F00O%2Fo")
print(driver.title)
#endregion

#region Tab+enter
search = driver.find_element(By.NAME, "username")#returns object that returns that represent the search bar. Find_element_by_name is the search command ()is what it searches.
search.send_keys("can do this for any site")#sends what you type into the page you pull up
search.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB)

#search.send_keys(Keys.RETURN)
#search.send_keys(Keys.TAB)#its takes 3 tabs
#search.send_keys(Keys.TAB)
#search.send_keys(Keys.TAB)
#search.send_keys(Keys.RETURN)#we are trying to tab into the SSO as opposed to using button element bc i cant figure out which element selects the SSO button.

time.sleep(3)
btn = driver.find_element(By.ID, "choose_idp")
btn.click()

time.sleep(3)

down = driver.find_element(By.ID, "s1")
down.send_keys(Keys.ARROW_DOWN)
#down.click()
#endregion

#region SFDL
#sf = driver.find_element(By.NAME, " ")#find the element on SF page to DL report
#sf.click()#figure out how to click whether its a link or button
#setup way to click where and how to save the CSV file may need to set up a driver for it
#export the CSV file to Python

#region CSV 
#Run in sales force to get repot and export to CSV. Use this with the file name for work comp. Once the file is ran here paste the file into the Badge Photo Metrics Dashboard in Quicksight
outfile = open("CID.csv", 'w')#the 'w' means write file
with open("Dragondata1.csv", 'r') as infile:#C://Users//mbern//Downloads//convertcsv.csv.xlsx. Relative vs Local Pathing. The 'r' is read only.
    reader = csv.reader(infile, delimiter= ",")#reads the csv one line at a time instead of the whole file at the same time
    header = next(reader)#next takes the current row converts it to a list and advances reader to the next row.
    for row in reader:#will have to set these up according to how the headers are in the SF report
     schedule = row[0]
     candidate_id = row[1]
     order_id = row[2]
     candidate_id_ =row[3]
     line = "{}\n".format(candidate_id_)
     outfile.write(line)

outfile.close()
#endregion 

#region QS access
time.sleep(3)
driver.get("https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/75622c93-5047-4c0a-8d1b-fe949ffb240d/sheets/75622c93-5047-4c0a-8d1b-fe949ffb240d_e5113b3e-e914-4783-b3f0-8ec12a16cdaf")
print(driver.title)
search2 = driver.find_element(By.ID, "account-name-input")
search2.send_keys("i need an account doe")
time.sleep(3)
search2.send_keys(Keys.RETURN)
time.sleep(2)
search2 = driver.find_element(By.ID, "username")
search2.send_keys("hi")
time.sleep(1)
search2.send_keys(Keys.TAB)
time.sleep(1)
search2 = driver.find_element(By.ID, "password")
search2.send_keys("password")
#search2.send_keys(Keys.RETURN)
time.sleep(1)
#endregion

#qs = driver.find_element(By.ID, "BPMD")#need to find the BPMD to click once inside qs and find the field audit tab
#qs.click()#find out if you need button or link and click this and then find FAT
#we should bein the fat now
#fat = driver.find.element(By.ID, "FAT")#same as before find the html for the field audit tab. here we need to paste the values from CID.csv into the BBCID
#fat.click()#paste the values from the CID.csv file we made earlier into the BBCID.
#we now find the BBCID field from html to paste the CID file
#bbcid =driver.find_element(By.ID, "")#find what the element tag is for the bbcid field
#bbcid.click()#click the field to enter the CSV values
#bbcid.send_keys(Keys.paste)#have to find out what the best way to paste is. can do a two button click if needed ctr+v
#once we have the file CID.csv copied into the fat

#driver.get("CID.csv")
#time.sleep(1)
open("CID.csv", 'r') 
time.sleep(3)
#cid2 = driver.get("CID.csv")
#time.sleep(1)
#cid2.send_keys(Keys.chord(Keys.CONTROL, "a"))
#time.sleep(2)
#cid2.send_keys(Keys.chord(Keys.CONTROL, "c"))

#region not used


#action = ActionChains(driver)
#action.key_down(Keys.ARROW_DOWN)

#failed btn attempt btn.send_keys(Keys.DOWN)
#search.send_keys(Keys.ENTER)


#sso = driver.find_element(By.CLASS_NAME, "idpli") 
#sso.click()
#print(sso.text)

#loads main waits and prints. finds element with id main and prints them
#try:
    #sso = WebDriverWait(driver, 10).until(
     #  EC.presence_of_element_located((By.XPATH,"button mb8 secondary wide"))
    #)
    #sso.click()

    #articles = main.find_elements_by_tag_name("article")
    #for article in articles:
                #header = article.find_element_by_class_name("entry-summary")
                #print(header.text)
#except:
    #driver.quit()
#endregion

#region quit
time.sleep(3)
driver.quit()
#endregion



