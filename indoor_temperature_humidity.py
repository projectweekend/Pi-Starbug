import dhtreader
import utils


TEMPERATURE_SENSOR_TYPE = 22
TEMPERATURE_SENSOR_PIN = 4


def send_humidity(humidity_value):
    url = "http://holly.local/api/indoor/humidity"
    humidity_data = {
        'percent': humidity_value
    }
    response = utils.make_json_post(url, humidity_data)
    if response != 201:
        # todo logging
        pass


def send_temperature(temperature_value):
    url = "http://holly.local/api/indoor/temperature" 
    temperature_data = {
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
    if result:
        send_temperature(result[0])
        send_humidity(result[1])
        print "Result was empty"
    return


if __name__ == "__main__":
    worker()
