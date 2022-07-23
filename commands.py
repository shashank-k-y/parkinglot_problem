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

        elif car.driver_age == driver_age:
            parking_slots.append(car.slot_number)

    return parking_slots


def get_slot_number_from_car_registration_number(
        parking_lot: object, registration_number: str
) -> list:
    parking_slots = []
    for car in parking_lot.slot_list:
        if not car:
            continue

        elif car.register_number == registration_number:
            parking_slots.append(car.slot_number)

    return parking_slots
