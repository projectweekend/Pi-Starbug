import holly
from stash import Stash


def process_temperature_data():
    temperature_stash = Stash("indoor_temperature")
    if temperature_stash.data:
        data_created = holly.send_bulk_temperature_data(temperature_stash.data)
        if data_created:
            temperature_stash.empty()
            return
    temperature_stash.close()


def process_humidity_data():
    humidity_stash = Stash("indoor_humidity")
    if humidity_stash.data:
        data_created = holly.send_bulk_humidity_data(humidity_stash.data)
        if data_created:
            humidity_stash.empty()
            return
    humidity_stash.close()


def process_system_temperature_data():
    system_temperature_stash = Stash("system_temperature")
    if system_temperature_stash.data:
        data_created = holly.send_bulk_system_temperature_data(system_temperature_stash.data)
        if data_created:
            system_temperature_stash.empty()
            return
    system_temperature_stash.close()


def worker():
    process_temperature_data()
    process_humidity_data()
    process_system_temperature_data()


if __name__ == "__main__":
    worker()
