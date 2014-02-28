import json
import subprocess
from hammock import Hammock

import utils


SHELL_COMMAND = ["/opt/vc/bin/vcgencmd", "measure_temp"]
API = Hammock('http://holly.local/api')


def get_system_temp():
    system_result = subprocess.check_output(SHELL_COMMAND)
    celsius_temp = utils.parse_temp_value(system_result)
    fahrenheit_temp = utils.celsius_to_fahrenheit(celsius_temp)
    return {'celsius':celsius_temp, 'fahrenheit': fahrenheit_temp}


def worker():
    system_temperature = get_system_temp()
    response = API.starbug.temperature.POST(data=json.dumps(system_temperature))
    if response.status_code != 201:
        # TODO...logging
        pass
    return


if __name__ == "__main__":
    worker()
