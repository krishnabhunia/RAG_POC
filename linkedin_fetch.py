from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("/path/to/chromedriver"))
driver.get("https://www.linkedin.com/login")
# → Manually login
input("Press Enter after login...")

driver.get("https://www.linkedin.com/search/results/people/?geoUrn=[\"107807598\",\"90009654\"]&origin=FACETED_SEARCH&page=2")

names = []
elements = driver.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text > a > span[aria-hidden='true']")
for e in elements:
    names.append(e.text.strip())

print(names)
driver.quit()