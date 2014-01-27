import dhtreader


SENSOR_TYPE = 22
SENSOR_PIN = 4

dhtreader.init()
print dhtreader.read(SENSOR_TYPE, SENSOR_PIN)

