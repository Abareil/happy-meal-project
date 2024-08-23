
from selenium.webdriver.common.keys import Keys
import time
from scraper import *

def main():

    driver = create_webdriver()
    navigate_to_page(driver, "https://www.mcdonalds.com.ar/pedidos/seleccionar-restaurante")

    search_field = find_element_by_css(driver, "input.input[placeholder='Escribe tu ciudad o tu dirección']")
    search_field.send_keys("Florida 281, Ciudad Autónoma de Buenos Aires")
    search_field.send_keys(Keys.RETURN)

    restaurant_div = find_element_by_xpath(driver, "//div[@class='mcd-restaurant-d-content']//p[contains(text(), 'Florida 281')]")
    container_div = restaurant_div.find_element(By.XPATH, "..//ancestor::div[@class='mcd-restaurant-d-content']")
    comenzar_pedido_button = container_div.find_element(By.XPATH, ".//button[contains(@class, 'is-primary')]")
    click_element(comenzar_pedido_button)

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.columns")))
    time.sleep(3)

    cajita_feliz_link = find_element_by_xpath(driver, "//ul[@class='columns is-multiline is-variable is-1']//a[contains(@href, 'cajita-feliz')]")
    click_element(cajita_feliz_link)

    cajita_feliz_item = find_element_by_css(driver, 'a#product-item26014', timeout=30)
    click_element(cajita_feliz_item)

    price_element = find_element_by_css(driver, "h5.is-hidden-touch", timeout=30)
    price_text = price_element.text

       # save_text_to_file(price_text, 'happy-meal-price.txt')
    print(price_text)

    save_price_to_dynamodb('happy-meal-price', price_text)

    time.sleep(5)
    driver.quit()

    return {"statusCode": 200, "body": "successful process"}

if __name__ == "__main__":
    main()



