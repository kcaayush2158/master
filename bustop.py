# Necessary variables
busCapacity = 47
totalPassengerInBus = 0
happyCustomer = 0
unhappyCustomer = 0
ratio = 0


# Ask route number and validate it
routeNumber = 0
while True:
    try:
        routeNumber = input("Enter the route number :")
        routeNumber = int(routeNumber)
        if routeNumber > 0:
            break
        else:
            raise Exception("number should be greater than 0")
    except:
        print("Please enter a valid number")


# Ask the number of bus stop and validate it
noOfStops = 0
while True:
    try:
        noOfStops = input("Please enter the number of stops on this route :")
        noOfStops = int(noOfStops)
        if noOfStops > 0:
            break
        else:
            raise Exception("Stop should be greater than 0")
    except ValueError:
        print("Please enter a valid number")


# Handling the customer joining and leaving the bus
i = 0
while i < noOfStops:

    # First bus stop
    # Customer only joins. They do not leave the bus
    if i == 0:
        while True:
            try:
                totalNumber = input(' How many passengers were waiting for the bus at stop #' + str(i + 1) + " : ")
                totalNumber = int(totalNumber)

                if totalNumber < 1:
                    raise Exception("Should be positive integer")

                if totalNumber > busCapacity:
                    totalPassengerInBus = busCapacity
                    unhappyCustomer = totalNumber - busCapacity
                    happyCustomer = busCapacity
                else:
                    happyCustomer = totalNumber
                    totalPassengerInBus = totalNumber

                i = i + 1
                break
            except:
                print("Enter a valid number")

    # This is the last stop
    # Customer only leave the bus here
    elif i == noOfStops - 1:
        while True:
            try:
                response = input("How many passengers left the bus at stop # " + str(i + 1) + " : ")
                response = int(response)
                if response < 1:
                    raise Exception("Number should be greater than 0")

                if response > busCapacity:
                    raise Exception("CANNOT HAVE MORE THAN BUS CAPACITY ")

                if response != totalPassengerInBus:
                    raise Exception("All the passenger" + totalPassengerInBus + "should leave bus in last stop")

                totalPassengerInBus = 0
                i = i + 1
                break
            except:
                print("Enter a valid number")
    
    # This is the bus stop between first and last stop
    else:
        while True:
            try:
                response = input("How many passengers are leaving the bus at stop #" + str(i + 1))
                response = int(response)
                if response < 0:
                    raise Exception("Should be a positive integer")

                if response > busCapacity:
                    raise Exception("Value should not be greater than bus capacity")

                if response > totalPassengerInBus:
                    raise Exception("There cannot more people leaving then they are inside the bus")

                totalPassengerInBus = totalPassengerInBus - response
                break
            except:
                print("Enter a valid number")

        while True:
            try:
                response = input("How many passengers are joining the bus at stop #" + str(i + 1))
                response = int(response)
                if response < 1:
                    raise Exception("Should be a positive integer")

                if response > busCapacity:
                    raise Exception("Bus Capacity should be lesser")

                if (response + totalPassengerInBus) > busCapacity:
                    unhappyCustomer += response + totalPassengerInBus - busCapacity
                    happyCustomer += busCapacity - totalPassengerInBus
                    totalPassengerInBus = busCapacity
                else:
                    happyCustomer += response
                    totalPassengerInBus += response
                break
            except:
                print("Enter a valid number")
        
        i = i + 1

print('------------------------------------------------------------------------------------')
print('                                  RESULT                                             ')
print('-------------------------------------------------------------------------------------')
print("Route number                                    :    " + str(routeNumber))
print("Happy customer                                  :    " + str(happyCustomer))
print("Unhappy customer                                :    " + str(unhappyCustomer))
if unhappyCustomer > 0:
    print("Ratio                                            :      " + str(happyCustomer / unhappyCustomer))
else:
    print("Ratio                                            :      " + str(0.00))
print('-------------------------------------------------------------------------------------')
