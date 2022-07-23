class ParkingLot():
    def __init__(self, max_slots):
        self.slot_list = [None] * max_slots


class Car():
    def __init__(self, register_number, driver_age, parking_lot):
        self.register_number = register_number
        self.driver_age = driver_age
        self.slot_number = self.assign_empty_slot(parking_lot=parking_lot) + 1

    def __str__(self) -> str:
        return f"{self.register_number}, {self.driver_age}, {self.slot_number}"

    def assign_empty_slot(self, parking_lot: object) -> int:
        slots = parking_lot.slot_list
        for i in range(len(slots)):
            if slots[i] is None:
                slots[i] = self
                return i
