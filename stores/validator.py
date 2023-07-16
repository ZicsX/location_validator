import re
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def find_store(latitude, longitude, radius):
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    
    # Make the API request
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type=store&keyword=shoppers%20Stop&key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Filter the results
    store_data = None
    if 'results' in data:
        results = data['results']
        for result in results:
            if 'name' in result and 'vicinity' in result and 'business_status' in result and 'types' in result and 'geometry' in result:
                store_name = result['name']
                vicinity = result['vicinity']
                business_status = result['business_status']
                types = result['types']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                if re.search(r'\bShoppers\sStop\b', store_name, re.IGNORECASE) and 'department_store' in types and business_status == 'OPERATIONAL':
                    store_data = {'name': store_name, 'address': vicinity, 'latitude': lat, 'longitude': lng}
                    break
    return store_data
