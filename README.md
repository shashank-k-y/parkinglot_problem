# Parkinglot problem

## Problem statement:
----------------------

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.
When a car enters the parking lot, we want to have a ticket issued to the driver.

### The ticket issuing process includes:- 

We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
And we are allocating an available parking slot to the car before actually handing over a ticket to the driver.
The customer should be allocated a parking slot that is nearest to the entry. At the exit, 
the customer returns the ticket, marking the slot they were using as being available.


### Due to government regulation, the system should provide us with the ability to find out:-

Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
Slot number in which a car with a given vehicle registration plate is parked. 
Slot numbers of all slots where cars of drivers of a particular age are parked.


## Sample Inputs:
----------------------
https://github.com/shashank-k-y/parkinglot_problem/blob/main/input.txt


## Sample Outputs:
----------------------
<img width="1092" alt="Screenshot 2022-07-23 at 9 24 10 PM" src="https://user-images.githubusercontent.com/74789167/180612685-1823ac73-3dc4-42d1-b7b6-b1d241350f3b.png">


## Execution:
--------------

step1:
    git clone https://github.com/shashank-k-y/parkinglot_problem.git

step2:
    cd parkinglot_problem
    
step3:
    python3 run_commands.py
    
step4:
    cheers 🍻 
