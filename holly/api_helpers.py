import utils


def send_bulk_humidity_data(humidity_data_list):
    url = "http://holly.local/api/indoor/humidity/bulk"
    post_data = {
        'humidity_data': humidity_data_list
    }
    response = utils.make_json_post(url, post_data)
    if response != 201:
        # todo logging
        return False
    return True


def send_bulk_temperature_data(temperature_data_list):
    url = "http://holly.local/api/indoor/temperature/bulk" 
    post_data = {
        'temperature_data': temperature_data_list
    }
    response = utils.make_json_post(url, post_data)
    if response != 201:
        # todo logging
        return False
    return True
