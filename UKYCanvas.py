from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

timeWait = 100

f = open("credentialsUKY.txt", "r")
lines = f.readlines()
email = str(lines[0])
pswd = str(lines[1])

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://adfs.uky.edu/adfs/ls?SAMLRequest=fZJfT8IwFMXf%2FRRL3%2FeXBUizkSDESIJKYPrgi%2Bm6O2jYWuxtVb693dCIifLY23Pu757bZsja5kCn1uzkGl4toPE%2B2kYi7S9yYrWkiqFAKlkLSA2nm%2BndkiZBRA9aGcVVQ84slx0MEbQRShJvMc%2FJC9RxOozLyOcwGvoppGO%2FrOPK56yMBpBCxUZAvCfQ6Dw5cS2cEdHCQqJh0rhSlER%2BHPlRUsRjOkhoEj0Tb%2B5yCMlM79oZc0AahqyqMbD7YwCV7Q9hg8Sbfo80UxJtC3oD%2Bk1weFwvf6x2HwhH1JYbqyHgqg0btRUy7CITb%2FW1iGshKyG3l3dQnkRIb4ti5a8eNgWZZF0f2ifTkw76N7NTJVl4Ls5OD3jvMIv5SjWCH70bpVtm%2Fp8iDuK%2BIiq%2F7qXUSjwAF7WAym2kadT7TAMzkBPHBxJOTtDfH2Vy9Qk%3D')
driver.maximize_window()

# Enter in Email on Outlook
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[1]/input')))
inputButton.click()
inputButton.send_keys(email)


# Enter in Password on Outlook
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input')))
inputButton.click()
inputButton.send_keys(pswd + Keys.RETURN)

# Open New Tab for portal
driver.execute_script(
    "window.open('https://login.microsoftonline.com/common/oauth2/authorize?client_id=09abbdfd-ed23-44ee-a2d9-a627aa1c90f3&resource=09abbdfd-ed23-44ee-a2d9-a627aa1c90f3&response_mode=form_post&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DARQCwlFUcnXMVy9wP2OJm57Jc4OIQxeg9jcQ9_ecRxkKjQ3DocUPQAemIREx_VH-0HtgHXFpkAUGj3lf7xRY1142Qekovpd5B45vvkIdm81x&nonce=637372605212627368.YTdlNzNhN2MtMmYzMy00MWRiLWJmMzYtYzEzZWM5NzZjMDA4NGJkYjA1OTUtYjlhYi00MjI1LTgzNmItMzZiMDA5OTM2ZDAx&redirect_uri=https%3A%2F%2Ftasks.office.com%2Flanding&ui_locales=en-US&mkt=en-US&x-client-SKU=ID_NET461&x-client-ver=6.5.0.0')")
driver.switch_to.window(driver.window_handles[1])
print('switched')
inputButton = WebDriverWait(driver,timeWait).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')))
print('Located')    
inputButton.click()
inputButton.send_keys(email + Keys.RETURN)


#Press Yes for Staying signed in
inputButton = WebDriverWait(driver,timeWait).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')))
inputButton.click()


#Open Email
driver.execute_script(
    "window.open('https://outlook.live.com/owa/')")
driver.switch_to.window(driver.window_handles[2])
inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a')))
inputButton.click()


inputButton = WebDriverWait(driver, timeWait).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))
inputButton.click()
inputButton.send_keys(email + Keys.RETURN)