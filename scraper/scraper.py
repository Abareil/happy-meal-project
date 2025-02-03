from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from datetime import datetime
from decimal import Decimal
import boto3
import json
load_dotenv()

def create_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    #que no sea visible el navegador
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def navigate_to_page(driver, url):
    driver.get(url)


def find_element_by_css(driver, css_selector, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )


def find_element_by_xpath(driver, xpath, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )


def click_element(element):
    element.click()
    return "click realizado"


def save_price_to_dynamodb(table_name, price_str):
    # Convert string to Decimal
    price_float = float(price_str.strip().replace('$', '').replace('.', '').replace(',', '.'))
    price_decimal = Decimal(price_float)

    # DB connection
    dynamodb = boto3.resource('dynamodb', region_name=os.getenv('REGION'))  # Especifica la región aquí
    table = dynamodb.Table(table_name)

    # item
    current_date = datetime.now().strftime('%Y-%m-%d')
    item = {
        'date': current_date,
        'price': price_decimal
    }

    # insert to DynamoDB
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps("Item saved successfully!")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error inserting item: {str(e)}')
        }

