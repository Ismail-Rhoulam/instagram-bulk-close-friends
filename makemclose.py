import os
import time
import getpass
import datetime
from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def typeThere(un, where):
    for k in un:
        where.send_keys(k)
    time.sleep(2)

def eraseThere(un, where):
    for _ in range(len(un)):
        where.send_keys(Keys.BACKSPACE)
    time.sleep(2)

def findExact(driver, mouse, un):
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{un}']")))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    mouse.move_to_element(element).click().perform()
    time.sleep(3)

USERNAME = input("Username: ")
PASSWORD = getpass.getpass("Password: ")

driver = uc.Chrome()
driver.maximize_window()
mouse = ActionChains(driver)
driver.get("https://www.instagram.com/")

os.makedirs(f"{datetime.date.today()}/{USERNAME}", exist_ok=True)

username = WebDriverWait(driver, 30).until(
    EC.any_of(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")),
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
    )
)
password = WebDriverWait(driver, 30).until(
    EC.any_of(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")),
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='pass']"))
    )
)

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

code = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='verificationCode']")))

CODE = input("Code de vérification: ")

code.send_keys(CODE)
code.send_keys(Keys.RETURN)

time.sleep(5)
print("Logged in")

time.sleep(15)
driver.get(f"https://www.instagram.com/{USERNAME}/")

fcount = int(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[starts-with(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span/span"))).text)
print(f'You have {fcount} followers')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{USERNAME}')]"))).click()
time.sleep(5)

scrolldiv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')))
scount = 0
while fcount > scount:
    for x in range(1000):
        scrolldiv.send_keys(Keys.ARROW_DOWN)
    felements = driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div[1]')
    scount = len(felements)


followers = [follower.text for follower in felements]
print(f'You\'ve collected {len(followers)} usernames')

with open(f"{datetime.date.today()}/{USERNAME}/followers.txt", "w") as f:
    f.write("\n".join(followers))

driver.get("https://www.instagram.com/accounts/close_friends/")
time.sleep(5)

search_section = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
failed = []
for uname in followers[942:]:
    try:
        typeThere(uname, search_section)
        time.sleep(2)
        findExact(driver, mouse, uname)
        time.sleep(3)
    except:
        print(f"Couldn't add {uname}")
        failed.append(uname)
    eraseThere(uname, search_section)
    time.sleep(2)

print("Done!")

if failed:
    print(f'Failed to add {len(failed)} followers')
    with open(f"{datetime.date.today()}/{USERNAME}/failed.txt", "w") as f:
        f.write("\n".join(failed))
else:
    print("All followers added")

driver.quit()