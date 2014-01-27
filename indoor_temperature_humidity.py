import dhtreader
import holly


TEMPERATURE_SENSOR_TYPE = 22
TEMPERATURE_SENSOR_PIN = 4    


def worker():
    dhtreader.init()
    result = dhtreader.read(TEMPERATURE_SENSOR_TYPE, TEMPERATURE_SENSOR_PIN)
    if result:
        holly.send_temperature(result[0])
        holly.send_humidity(result[1])
        print "Result was empty"
    return


if __name__ == "__main__":
    worker()
