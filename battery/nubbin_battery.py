from abc import ABC

from car import Car

from datetime import datetime


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date):
        current_date = datetime.today().date()
        super().__init__(last_service_date,current_date)
        self.current_date = current_date
        last_service_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        return self.current_date > self.last_service_date

