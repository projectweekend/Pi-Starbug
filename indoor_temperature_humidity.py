import datetime
import os

import dhtreader
import utils


TEMPERATURE_SENSOR_TYPE = int(os.getenv('TEMPERATURE_SENSOR_TYPE', 0))
TEMPERATURE_SENSOR_PIN = int(os.getenv('TEMPERATURE_SENSOR_PIN', 0))


def send_humidity(humidity_value):
    url = "http://holly.local/api/indoor/humidity"
    humidity_data = {
        'date': datetime.datetime.now(),
        'percent': humidity_value
    }
    response = utils.make_json_post(url, humidity_data)
    if response != 201:
        # todo logging
        pass


def send_temperature(temperature_value):
    url = "http://holly.local/api/indoor/temperature" 
    temperature_data = {
        'date': datetime.datetime.now(),
        'celsius': temperature_value,
        'fahrenheit': utils.celsius_to_fahrenheit(temperature_value)
    }
    response = utils.make_json_post(url, temperature_data)
    if response != 201:
        # todo logging
        pass    


def worker():
    dhtreader.init()
    result = dhtreader.read(TEMPERATURE_SENSOR_TYPE, TEMPERATURE_SENSOR_PIN)
    send_temperature(result[0])
    send_humidity(result[1])


if __name__ == "__main__":
    worker()
