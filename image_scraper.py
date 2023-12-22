from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import io
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
# Assuming options is an instance of ChromeOptions
options = webdriver.ChromeOptions()

# ... add any other options you need ...
options.add_argument("--incognito")
chrome_service = webdriver.chrome.service.Service(
    ChromeDriverManager().install())
# Now, use webdriver_manager to get the appropriate driver


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_bytes = io.BytesIO(image_content)
        image = Image.open(image_bytes)
        file_path = download_path + r"\\" + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Scraping was successful")
    except Exception as e:
        print('Scraping failed', e)


# url_test = "https://images.unsplash.com/photo-1552053831-71594a27632d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRvZ3N8ZW58MHx8MHx8fDA%3D"
# https://images.unsplash.com/photo-1552053831-71594a27632d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRvZ3N8ZW58MHx8MHx8fDA%3D
# download_image(
    # r"C:\Users\Vedant\Desktop\Ip_Internship\test-images", url_test, "dog.jpeg")


def scraper(page_no, keywords):
    url = f"https://www.freeimages.com/search/{keywords}/{page_no}"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    pictures = driver.find_elements(
        By.CLASS_NAME, "grid-thumb")
    c = 1
    for pic in pictures:
        image_url = pic.get_attribute("src")
        download_image(r"C:\Users\Vedant\Desktop\Ip_Internship\test-images",
                       image_url, f"{keywords}_{page_no}_{c}.jpeg")
        c += 1

    driver.close()


keywords = input("Enter the keyword: ")
no_of_pages = int(input("Enter the number of pages to be scraped: "))
for i in range(1, no_of_pages+1):
    scraper(i, keywords)
