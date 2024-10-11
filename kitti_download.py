import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
import requests

# Function to download all images from a dynamically loaded page
def download_images_selenium(url, folder_name):
    # Create the folder to store the images
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Set up the Selenium WebDriver (using Chrome)
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in PATH
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)  # Adjust time based on your internet speed or page load time

    # Find all the image elements (You may need to adjust the selector based on the webpage structure)
    images = driver.find_elements(By.TAG_NAME, "img")

    # Download each image
    for img in images:
        # Get the image URL from the 'src' attribute
        img_url = img.get_attribute("src")
        if img_url:
            # Download the image
            img_name = os.path.join(folder_name, img_url.split("/")[-1])

            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(img_name, "wb") as f:
                    f.write(img_response.content)
                print(f"Downloaded: {img_name}")
            else:
                print(f"Failed to download: {img_url}")

    # Close the browser
    driver.quit()

# Example usage
webpage_url = 'https://app.visual-layer.com/dataset/f246c942-2bcb-11ef-9e12-4e52fc95a50e/data/cluster/9b4421eb-70c2-4efe-aa3c-5f4424359672?d_page=1'
download_folder = 'kitti_15-images'
download_images_selenium(webpage_url, download_folder)

