from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

# path = '/Users/krishna/Downloads/chromedriver-mac-x64/chromedriver'
# driver = webdriver.Chrome(service=Service(path))
driver.get("https://www.linkedin.com/login")
# → Manually login
input("Press Enter after login...")

linked_serach_path = "https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=2&sid=_et"
driver.get(linked_serach_path)
print(driver)

names = []

elements = driver.find_elements()
print(elements)

elements = driver.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text > a > span[aria-hidden='true']")
print(elements)

for e in elements:
    print(e.text.strip())
    names.append(e.text.strip())

print(names)
driver.quit()