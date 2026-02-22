import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalAmount)

assert Sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode"))).click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

DisAmt = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
print(DisAmt)
print(type(DisAmt))

assert DisAmt < totalAmount







#assert int(discountAmt) < totalAmount


#driver.find_element(By.CSS_SELECTOR, ".discountAmt").text()
#print(discountAmount)


#assert int(discountAmount) < totalAmount

time.sleep(5)
