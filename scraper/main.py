from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait


from scraper import *
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    driver = create_webdriver()

    # Navegar a la página principal
    navigate_to_page(driver, "https://www.mcdonalds.com.ar/restaurantes/ciudad-autonoma-de-buenos-aires/florida-281-fl2/pedidos")
    time.sleep(60)
    # click en cajita feliz
    cajitaFeliz_button = find_element_by_xpath(driver, '//*[@id="main-content"]/section/section[1]/div/div/div[4]/a')
    cajitaFeliz_button.click()
    time.sleep(10)
    # click en cajita feliz con hamburguesa
    cajitaFelizConHamburguesa_button = find_element_by_xpath(driver, '//*[@id="main-content"]/section/section[2]/div/a[3]')
    cajitaFelizConHamburguesa_button.click()

    #extraer precio
    price_element = find_element_by_xpath(driver, '//*[@id="main-content"]/section/div/section[1]/div/div/section/div[1]/div[2]')
    price_text = price_element.text

    time.sleep(3)
    driver.quit()

       # save_text_to_file(price_text, 'happy-meal-price.txt')
    print(price_text)

    save_price_to_dynamodb(os.getenv('TABLE_NAME'), price_text)

    driver.quit()

    return {"statusCode": 200, "body": "successful process"}


if __name__ == "__main__":
    main()






