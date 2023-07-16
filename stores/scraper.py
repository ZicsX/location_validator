import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .models import Store

def scrape_store_data(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    map_canvas = driver.find_element_by_id('map_canvas')

    store_data_json = map_canvas.get_attribute('data-stores')

    store_data = json.loads(store_data_json)

    for store in store_data['data']:
        new_store = Store(
            id=store['id'],
            latitude=store['latitude'],
            longitude=store['longitude'],
            name=store['name']
        )
        new_store.save()

    driver.quit()
