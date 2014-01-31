import subprocess

import utils


SHELL_COMMAND = ["/opt/vc/bin/vcgencmd", "measure_temp"]
API_URL = "http://holly.local/api/starbug/temperature"


def get_system_temp():
    system_result = subprocess.check_output(SHELL_COMMAND)
    celsius_temp = utils.parse_temp_value(system_result)
    fahrenheit_temp = utils.celsius_to_fahrenheit(celsius_temp)
    return {'celsius':celsius_temp, 'fahrenheit': fahrenheit_temp}


def worker():
    system_temperature = get_system_temp()
    response = utils.make_json_post(API_URL, system_temperature)
    if response != 201:
        # TODO...logging
        pass
    return


if __name__ == "__main__":
    worker()
