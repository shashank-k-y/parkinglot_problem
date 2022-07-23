from collections import namedtuple
from parking_lot import ParkingLot, Car


def create_parking_lot(max_slots: int) -> object:
    return ParkingLot(max_slots=max_slots)


def allocate_slot_to_car(
        register_number: str, driver_age: int, parking_lot: object
) -> object:
    return Car(
        register_number=register_number, driver_age=driver_age,
        parking_lot=parking_lot
    )


def get_slot_numbers_from_driver_age(
        parking_lot: object, driver_age: int
) -> list:
    parking_slots = []
    for car in parking_lot.slot_list:
        if not car:
            continue

        if car.driver_age == driver_age:
            parking_slots.append(car.slot_number)

    return parking_slots


def get_slot_number_from_car_registration_number(
        parking_lot: object, registration_number: str
) -> list:
    parking_slots = []
    for car in parking_lot.slot_list:
        if not car:
            continue

        if car.register_number == registration_number:
            parking_slots.append(car.slot_number)

    return parking_slots


def exit_car_make_space_available(
        parking_lot: object, parking_slot: int
) -> list:
    slot_list = parking_lot.slot_list
    car_details = namedtuple('car', ['register_number', "driver_age"])

    for car in slot_list:
        if not car:
            continue

        if car.slot_number == parking_slot:
            slot_list[parking_slot - 1] = None
            car_info = car_details(car.register_number, car.driver_age)
            break

    return car_info


def get_registration_number_from_driver_age(
        slot_list: list, driver_age: int
) -> tuple:
    register_numbers = []
    slot_numbers = []

    for car in slot_list:
        if not car:
            continue

        if car.driver_age == driver_age:
            register_numbers.append(car.register_number)
            slot_numbers.append(car.slot_number)

    return register_numbers, slot_numbers


def check_car_object_already_exists(register_number: str, slot_list: list):
    car_already_exists = False
    for car in slot_list:
        if not car:
            continue

        if car.register_number == register_number:
            car_already_exists = True
            break

    return car_already_exists
