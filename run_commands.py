from commands import (
    create_parking_lot,
    allocate_slot_to_car,
    get_slot_numbers_from_driver_age,
    get_slot_number_from_car_registration_number
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

    elif command[0] == 'Park':
        register_number = command[1]
        driver_age = int(command[3])
        if not parking_lot:
            print("please create a Parking lot with definate slots")
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
