import dhtreader


SENSOR_TYPE = 22
SENSOR_PIN = 4


def worker():
    dhtreader.init()
    result = dhtreader.read(SENSOR_TYPE, SENSOR_PIN)
    return result


if __name__ == "__main__":
    worker()
