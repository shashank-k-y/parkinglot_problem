from functions import (
    create_parking_lot,
    allocate_slot_to_car,
    get_slot_numbers_from_driver_age,
    get_slot_number_from_car_registration_number,
    exit_car_make_space_available,
    get_registration_number_from_driver_age,
    check_car_object_already_exists
)

parking_lot = None

while True:
    command = str(input("enter the command: ")).split(' ')
    if command[0] == 'exit':
        break

    if not command[0] == "Create_parking_lot":
        print("please create a parkinglot first or please check the command")
        continue

    try:
        max_slots = int(command[1])
    except ValueError:
        print("please give an integer value to the parking slots")

    parking_lot = create_parking_lot(max_slots=max_slots)
    print(f'Created parking of {max_slots} slots')
    break

while True:
    command = str(input("Enter the command: ")).split(' ')
    if command[0] == 'exit':
        break

    if not parking_lot:
        print("please create a Parking lot with definate slots")
        continue

    if command[0] == "Create_parking_lot":
        print("parking_lot already created, please use other commands")

    elif command[0] == 'Park':
        register_number = command[1]
        driver_age = int(command[3])

        slot_list = parking_lot.slot_list
        free_space = any(slot is None for slot in slot_list)
        if not free_space:
            print("Parking lot is full, please wait.")
            continue

        car_already_exists = check_car_object_already_exists(
            register_number=register_number, slot_list=slot_list
        )
        if car_already_exists:
            print(
                f"The car with registered number {register_number} " +
                "already parked"
            )
            continue

        car = allocate_slot_to_car(
            register_number=register_number, driver_age=driver_age,
            parking_lot=parking_lot
        )
        print(
            f"Car with vehicle registration number {car.register_number}" +
            f"has been parked at slot number {car.slot_number}"
        )

    elif command[0] == "Slot_numbers_for_driver_of_age":
        try:
            driver_age = int(command[1])
        except ValueError:
            print("driver age should be an integer")
            continue

        slot_numbers = get_slot_numbers_from_driver_age(
            parking_lot=parking_lot, driver_age=driver_age
        )
        if not slot_numbers:
            print(f"No slots found for driver age {driver_age}")
            continue

        print(",".join(str(slot) for slot in slot_numbers))

    elif command[0] == "Slot_number_for_car_with_number":
        register_number = command[1]

        slot_numbers = get_slot_number_from_car_registration_number(
            parking_lot=parking_lot, registration_number=register_number
        )
        if not slot_numbers:
            print(f"No slots found for registration number{register_number}")
            continue

        print(",".join(str(slot) for slot in slot_numbers))

    elif command[0] == "Leave":
        slot = int(command[1])
        car_details = exit_car_make_space_available(
            parking_lot=parking_lot, parking_slot=slot
        )
        if not car_details:
            print(f"no car is parked in slot {slot}")
            continue

        print(
            f"Slot number {slot} vacated, " +
            "the car with vehicle registration number " +
            f"{car_details.register_number} " +
            "left the space,the driver of the car was of age" +
            f"{car_details.driver_age}"
        )

    elif command[0] == "Vehicle_registration_number_for_driver_of_age":
        driver_age = int(command[1])
        registration_numbers, slots = get_registration_number_from_driver_age(
            slot_list=parking_lot.slot_list, driver_age=driver_age
        )
        if not registration_numbers:
            print(f"no vehicals where found where driver age is {driver_age}")
            continue

        reg_numbers = ','.join(number for number in registration_numbers)
        slot_numbers = ','.join(str(number) for number in slots)

        print(
            f"Car with vehicle registration number {reg_numbers} " +
            f"has been parked at slot number {slot_numbers}")

    else:
        print("please use accurate commands")
