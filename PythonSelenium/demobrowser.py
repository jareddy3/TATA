from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("Ferrar Nagar ")









































