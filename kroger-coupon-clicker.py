#  ----------------------
# | kroger coupon clicker
# | by rick kemery
# | will login to kroger website and click all the digital coupons for you (up to max loaded)
# | modify options.binary_location to match your chrome installation
# | modify options.add_argument for your chrome user data folder
# | enter username.send_keys as email address, password.send_keys as your kroger password
# | requires chromedriver found here: https://chromedriver.chromium.org/downloads
#  ----------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome Dev/Application/chrome.exe"
options.add_argument(r'user-data-dir=C:\Users\cooluser\AppData\Local\Google\Chrome Dev\User Data')

driver_path = "C:/Windows/chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.kroger.com/signin?redirectUrl=/cl/coupons/")

assert "Kroger" in driver.title

username = driver.find_element_by_name("email")
username.clear()
username.send_keys("e-n-t-e-r y-o-u-r e-m-a-i-l a-d-d-r-e-s-s h-e-r-e")
time.sleep(3)
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("e-n-t-e-r y-o-u-r p-a-s-s-w-o-r-d h-e-r-e")
time.sleep(3)
driver.find_element_by_id("SignIn-submitButton").click()
time.sleep(15)
buttons = driver.find_elements_by_xpath("//*[contains(@class, 'CouponButton')]")

for btn in buttons:
    btn.click()
time.sleep(10)
driver.refresh()
time.sleep(10)
buttons = driver.find_elements_by_xpath("//*[contains(@class, 'CouponButton')]")

for btn in buttons:
    btn.click()