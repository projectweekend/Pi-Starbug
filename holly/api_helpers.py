import utils


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
