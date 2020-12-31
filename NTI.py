from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

timeWait = 100

f = open("credentialsNTI.txt", "r")
lines = f.readlines()
email = str(lines[0])
pswd = str(lines[1])

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.maximize_window()

# Enter in Email on Google
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
inputButton.send_keys(email + Keys.RETURN)

# Enter in Email on Outlook
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))
inputButton.click()
inputButton.send_keys(email + Keys.RETURN)

# Enter in Password on Outlook
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input')))
inputButton.click()
inputButton.send_keys(pswd + Keys.RETURN)

# Open New Tab for email
driver.execute_script(
    "window.open('https://outlook.live.com/owa/')")
driver.switch_to.window(driver.window_handles[1])
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a')))
inputButton.click()


inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')))
inputButton.click()
inputButton.send_keys(email + Keys.RETURN)

# Open New Tab for portal
driver.execute_script(
    "window.open('https://docs.google.com/spreadsheets/d/1U-1lzZKKu8WOsR662vHx9l65CQLuTu3xgS3OKyBz_9I/edit#gid=0')")


