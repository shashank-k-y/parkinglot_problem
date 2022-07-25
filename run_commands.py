from parking_lot import ParkingLot

parking_lot = None


def run_command(command, parking_lot=parking_lot):
    command = command.split(' ')
    if command[0] == 'exit':
        return

    if not parking_lot and command[0] == "Create_parking_lot":
        try:
            max_slots = int(command[1])
        except ValueError:
            print("please give an integer value to the parking slots")
            return parking_lot

        parking_lot = ParkingLot.create_parking_lot(max_slots=max_slots)
        print(f'Created parking lot of {max_slots} slots')
        return parking_lot

    elif parking_lot and command[0] == "Create_parking_lot":
        print("parking_lot already created, please use other commands")
        return parking_lot

    elif not parking_lot and command[0] != "Create_parking_lot":
        print("please create a parkinglot first or please check the command")
        return parking_lot

    elif command[0] == 'Park':
        register_number = command[1]
        driver_age = int(command[3])

        slot_list = parking_lot.slot_list
        free_space = any(slot is None for slot in slot_list)
        if not free_space:
            print("Parking lot is full, please wait.")
            return parking_lot

        car_already_exists = parking_lot.check_car_object_already_exists(
            register_number=register_number,
        )
        if car_already_exists:
            print(
                f"The car with registered number {register_number} " +
                "already parked"
            )
            return parking_lot

        car = parking_lot.allocate_slot_to_car(
            register_number=register_number, driver_age=driver_age,
        )
        print(
            f"Car with vehicle registration number {car.register_number}" +
            f"has been parked at slot number {car.slot_number}"
        )
        return parking_lot

    elif command[0] == "Slot_numbers_for_driver_of_age":
        try:
            driver_age = int(command[1])
        except ValueError:
            print("driver age should be an integer")
            return parking_lot

        slot_numbers = parking_lot.get_slot_numbers_from_driver_age(
            driver_age=driver_age
        )
        if not slot_numbers:
            print(f"No slots found for driver age {driver_age}")

        print(",".join(str(slot) for slot in slot_numbers))
        return parking_lot

    elif command[0] == "Slot_number_for_car_with_number":
        register_number = command[1]

        slot_numbers = parking_lot.get_slot_from_registration_number(
            registration_number=register_number
        )
        if not slot_numbers:
            print(f"No slots found for registration number{register_number}")

        print(",".join(str(slot) for slot in slot_numbers))
        return parking_lot

    elif command[0] == "Leave":
        slot = int(command[1])
        car_details = parking_lot.exit_car_make_space_available(
            parking_slot=slot
        )
        if not car_details:
            print(f"no car is parked in slot {slot}")
            return parking_lot

        print(
            f"Slot number {slot} vacated, " +
            "the car with vehicle registration number " +
            f"{car_details.register_number} " +
            "left the space,the driver of the car was of age" +
            f"{car_details.driver_age}"
        )
        return parking_lot

    elif command[0] == "Vehicle_registration_number_for_driver_of_age":
        driver_age = int(command[1])
        registration_numbers, slots = parking_lot.get_registration_number_from_driver_age(  # noqa
            driver_age=driver_age
        )
        if not registration_numbers:
            print(f"no vehicals where found where driver age is {driver_age}")
            return parking_lot

        reg_numbers = ','.join(number for number in registration_numbers)
        slot_numbers = ','.join(str(number) for number in slots)

        print(
            f"The driver of age {driver_age} has vehicle " +
            f"registration number {reg_numbers} " +
            f"has been parked at slot number {slot_numbers}"
        )
        return parking_lot

    else:
        print("please use accurate commands")
        return parking_lot


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        parking_lot = run_command(command=line, parking_lot=parking_lot)
