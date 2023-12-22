from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import io
from PIL import Image
# Assuming options is an instance of ChromeOptions
options = webdriver.ChromeOptions()

# ... add any other options you need ...
options.add_argument("--incognito")
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
# Now, use webdriver_manager to get the appropriate driver
driver = webdriver.Chrome(service=chrome_service, options=options)


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_bytes = io.BytesIO(image_content)
		image = Image.open(image_bytes)
		file_path = download_path + r"\ " +file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Scraping was successful")
	except Exception as e:
		print('Scraping failed', e)
		
url_test="https://images.unsplash.com/photo-1552053831-71594a27632d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRvZ3N8ZW58MHx8MHx8fDA%3D"
download_image(r"D:\Internship\test-images",url_test,"dog.jpeg")