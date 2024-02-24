from selenium import webdriver
import re
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


#Set up the Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# URL of the website you want to open (Student Registration Form)
driver.get('https://tummytruck.com.np/')
driver.implicitly_wait(10)

# Maximize the browser window
driver.maximize_window()

# Calculate the height of the webpage
page_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down the webpage slowly using JavaScript
scroll_speed = 50
scroll_iterations = int(page_height / scroll_speed)

for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
time.sleep(2)

#get to aboutus page
driver.get('https://tummytruck.com.np/aboutus')


def is_valid_email(email):
 try:
  email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

  if re.search(email_pattern, email):
   return True
  else:
   return False
 except Exception as e:
  print(e)
  return False

email_field = driver.find_element(*(By.XPATH,"//input[@id='email']")).send_keys('automation@gmail.com')
submit_button = driver.find_element(*(By.XPATH,"//button[normalize-space()='Submit']"))
submit_button.click()
time.sleep(5)

#automate contact us page
driver.get('https://tummytruck.com.np/contactus')
time.sleep(2)
your_name_field = driver.find_element(*(By.XPATH,"//input[@id='name']")).send_keys('Rabeendra')
time.sleep(2)
your_contact_field = driver.find_element(*(By.XPATH,"//input[@id='contact']")).send_keys('1234567890')
time.sleep(2)
your_query_field = driver.find_element(*(By.XPATH,"//textarea[@id='query']")).send_keys('what is the price for the non-veg meal package for a month')
time.sleep(5)
send_message_button = driver.find_element(*(By.XPATH,"//button[normalize-space()='Send message']"))
send_message_button.click()
time.sleep(5)

driver.get('https://tummytruck.com.np/#menu')
time.sleep(2)
page_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down the webpage slowly using JavaScript
scroll_speed = 120
scroll_iterations = int(page_height / scroll_speed)

for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
time.sleep(3)

green_first_week = driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[1]//div[1]//span[1]//img[1]")).click()
time.sleep(2)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(3)
driver.back()
time.sleep(3)

green_second_week = driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[2]//div[1]//span[1]//img[1]")).click()
time.sleep(2)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(3)

green_third_week = driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[3]//div[1]//span[1]//img[1]")).click()
time.sleep(2)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(3)

yummy_first_week = driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[1]//div[1]//span[1]//img[1]")).click()
time.sleep(2)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(3)

yummy_second_week = driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[2]//div[1]//span[1]//img[1]")).click()
time.sleep(2)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()

scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)

for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
time.sleep(5)

pro_first_week = driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[1]//div[1]//span[1]//img[1]")).click()
time.sleep(5)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(5)

pro_second_week = driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[2]//div[1]//span[1]//img[1]")).click()
time.sleep(5)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(5)

pro_forth_week = driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[4]//div[1]//span[1]//img[1]")).click()
time.sleep(5)
scroll_speed = 200
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
 driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
 time.sleep(2)
driver.back()
time.sleep(5)



# Close the WebDriver instance
driver.quit()
print("Congrats!! code run successfully")