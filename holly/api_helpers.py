import json
from hammock import Hammock

API = Hammock('http://holly.local/api')
API_HEADERS = {'Content-type': 'application/json'}


def send_bulk_humidity_data(humidity_data_list):
    post_data = json.dumps({'humidity_data': humidity_data_list})
    response = API.indoor.humidity.bulk.POST(data=post_data, headers=API_HEADERS)
    if response.status_code != 201:
        # todo logging
        return False
    return True


def send_bulk_temperature_data(temperature_data_list):
    post_data = json.dumps({'temperature_data': temperature_data_list})
    response = API.indoor.temperature.bulk.POST(data=post_data, headers=API_HEADERS)
    if response.status_code != 201:
        # todo logging
        return False
    return True


def send_bulk_system_temperature_data(temperature_data_list):
    post_data = json.dumps({'temperature_data': temperature_data_list})
    response = API.starbug.temperature.bulk.POST(data=post_data, headers=API_HEADERS)
    if response.status_code != 201:
        # todo logging
        return False
    return True    
