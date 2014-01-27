import holly
from stash import Stash


def process_temperature_data():
    stash = Stash("indoor_temperature")
    data_created = holly.send_bulk_temperature_data(stash.data)
    if data_created:
        stash.empty()


def process_humidity_data():
    stash = Stash("indoor_humidity")
    data_created = holly.send_bulk_humidity_data(stash.data)
    if data_created:
        stash.empty()


def worker():
    process_temperature_data()
    process_humidity_data()


if __name__ == "__main__":
    worker()
