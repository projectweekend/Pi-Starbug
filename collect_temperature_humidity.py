import time
import datetime

import dhtreader
import utils
from stash import Stash


TEMPERATURE_SENSOR_TYPE = 22
TEMPERATURE_SENSOR_PIN = 4


def get_sensor_data():
    return dhtreader.read(TEMPERATURE_SENSOR_TYPE, TEMPERATURE_SENSOR_PIN)


def stash_temperature(temperature_value):
    temperature_stash = Stash("indoor_temperature")
    temperature_data = {
        'date': datetime.datetime.utcnow().isoformat(),
        'celsius': temperature_value,
        'fahrenheit': utils.celsius_to_fahrenheit(temperature_value)
    }
    temperature_stash.add(temperature_data)


def stash_humidity(humidity_value):
    humidity_stash = Stash("indoor_humidity")
    humidity_data = {
        'date': datetime.datetime.utcnow().isoformat(),
        'percent': humidity_value
    }
    humidity_stash.add(humidity_data)


def worker():
    dhtreader.init()
    # try this multiple times because we don't always get data on first attempt
    # the python driver for this sensor is still experimental
    for x in range(10):
        result = get_sensor_data()
        if result:
            # stash the data we found and exit
            stash_temperature(result[0])
            stash_humidity(result[1])
            break
        # wait 10 seconds before attempting another sensor reading
        time.sleep(10)


if __name__ == "__main__":
    worker()
