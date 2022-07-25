class ParkingLot():
    def __init__(self, max_slots):
        self.slot_list = [None] * max_slots

    @staticmethod
    def create_parking_lot(max_slots: int) -> object:
        return ParkingLot(max_slots=max_slots)

    def allocate_slot_to_car(
        self, register_number: str, driver_age: int
    ) -> object:
        return Car(
            register_number=register_number, driver_age=driver_age,
            parking_lot=self
        )

    def get_slot_numbers_from_driver_age(self, driver_age: int) -> list:
        parking_slots = []
        for car in self.slot_list:
            if not car:
                continue

            if car.driver_age == driver_age:
                parking_slots.append(car.slot_number)

        return parking_slots

    def get_slot_from_registration_number(
        self, registration_number: str
    ) -> list:
        parking_slots = []
        for car in self.slot_list:
            if not car:
                continue

            if car.register_number == registration_number:
                parking_slots.append(car.slot_number)

        return parking_slots

    def exit_car_make_space_available(self, parking_slot: int) -> object:
        slot_list = self.slot_list
        car_object = None

        for car in slot_list:
            if not car:
                continue

            if car.slot_number == parking_slot:
                slot_list[parking_slot - 1] = None
                car_object = car
                break

        return car_object

    def get_registration_number_from_driver_age(
            self, driver_age: int
    ) -> tuple:
        register_numbers = []
        slot_numbers = []

        for car in self.slot_list:
            if not car:
                continue

            if car.driver_age == driver_age:
                register_numbers.append(car.register_number)
                slot_numbers.append(car.slot_number)

        return register_numbers, slot_numbers

    def check_car_object_already_exists(self, register_number: str) -> bool:
        car_already_exists = False
        for car in self.slot_list:
            if not car:
                continue

            if car.register_number == register_number:
                car_already_exists = True
                break

        return car_already_exists


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
