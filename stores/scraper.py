import json
from .models import Store
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .validator import find_store


def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_store_data(url):
    driver = setup_driver()
    driver.get(url)

    map_canvas = driver.find_element(By.ID, 'map_canvas')

    store_data_json = map_canvas.get_attribute('data-stores')

    store_data = json.loads(store_data_json)

    for store in store_data['data'][:5]: # remove slicing in prod
        validated_store = find_store(store['latitude'], store['longitude'], 50)

        if validated_store:
            # Create a new Store object for each store
            new_store = Store(id=store['id'],
                              name=store['name'],
                              address = validated_store['address'],
                              latitude=validated_store['latitude'],
                              longitude=validated_store['longitude'],
                              is_verified=True
                            )
        else:
            new_store = Store(id=store['id'],
                              name=store['name'],
                              latitude=store['latitude'],
                              longitude=store['longitude'],
                              is_verified=False
                            )
        # Save the new Store object to the database
        new_store.save()

    # Close the browser
    driver.quit()
