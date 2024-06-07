from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json


def scraping():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Download the webdriver
    service = Service("chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("http://bianca.com")

    # Extract content (example: title of the page)
    title = driver.title

    driver.quit()

    return {
        'statusCode': 200,
        'body': json.dumps({'title': title})
    }


print(scraping())
