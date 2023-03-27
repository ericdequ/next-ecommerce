import os
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.bing.com/create?toWww=1&redig=30C04FC20A7A4BA08168CC7BB17EDFD6"
SAVE_PATH = "C:/dev/personal/ecom/next_DBC/public/dbc_products"
CHROME_DRIVER_PATH = "C:/path/to/chromedriver.exe"

products= [
    "Reishi Mushroom Tincture",
    "Delta 8 Tincture",
  ]

image_xpaths = [
    '//*[@id="mmComponent_images_1"]/ul[1]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[1]/li[2]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[2]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[2]/li[2]/div/div/a/div/img'
]

def main():
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    for product in products:
        driver.get(BASE_URL)

        try:
            login_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]/div/div/div/div[4]/div/div/div/div[2]/a'))
            )
            login_button.click()
            print("Logging in with Face...")
            time.sleep(5)
        except Exception as e:
            print("No login required, continuing...")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]'))
        )
        search_box.clear()
        search_box.send_keys(f"can you make a stunning product image for {product}")
        search_box.submit()

        product_folder = os.path.join(SAVE_PATH, product.replace(" ", "_"))
        os.makedirs(product_folder, exist_ok=True)

        for index, xpath in enumerate(image_xpaths, start=1):
            print(f"Waiting for image {index} to be generated for {product}...")
            try:
                generated_image = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                generated_image_url = generated_image.get_attribute("src")

                response = request.urlopen(generated_image_url)
                if response.status == 200:
                    print(f"Saving image {index} for {product}...")
                    with open(os.path.join(product_folder, f"{product.replace(' ', '_')}_img{index}.jpg"), "wb") as file:
                        file.write(response.read())
                    print(f"Image {index} for {product} saved successfully.")
                else:
                    print(f"Failed to download image {index} for {product} (status code {response.status}).")
            except Exception as e:
              print(f"Error while downloading image {index} for {product}: {e}")
    driver.quit()

if __name__ == "__main__":
  main()
  main()






