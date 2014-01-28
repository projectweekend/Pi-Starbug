import holly
from stash import Stash


def process_temperature_data():
    temperature_stash = Stash("indoor_temperature")
    data_created = holly.send_bulk_temperature_data(temperature_stash.data)
    if data_created:
        temperature_stash.empty()


def process_humidity_data():
    humidity_stash = Stash("indoor_humidity")
    data_created = holly.send_bulk_humidity_data(humidity_stash.data)
    if data_created:
        humidity_stash.empty()


def worker():
    process_temperature_data()
    process_humidity_data()


if __name__ == "__main__":
    worker()
