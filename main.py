from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('https://www.silive.com/highschoolsports/2023/04/poll-who-will-be-the-best-hs-baseball-hitter-this-season.html')

while True:
    driver.refresh()
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    option_id = 'PDI_answer54922355'
    option = soup.find('input', {'id': option_id})
    if option:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, option_id)))
        element.click()
    time.sleep(2)
    option_id2 = 'pd-vote-button12103015'
    option2 = soup.find('div', {'class': 'css-votebutton-outer'})
    if option2:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, option_id2)))
        element.click()
    time.sleep(2)

driver.quit()

