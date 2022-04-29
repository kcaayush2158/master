busCapacity = 47
totalPassengerInBus = 0
happyCustomer = 0
unhappyCustomer = 0
ratio = 0
routeNumber = 0
noOfStops = 0

while True:
    routeNumber = input("Enter the route number :")
    try:
        routeNumber = int(routeNumber);
        if routeNumber > 0:
            break;
        else:
            raise Exception("number should be greater than 0")
    except ValueError:
        print("Please enter a valid number")

while True:
    noOfStops = input("Please enter the number of stops on this route :")
    try:
        noOfStops = int(noOfStops);
        if noOfStops > 0:
            break;
        else:
            raise Exception("Stop should be greater than 0")
    except ValueError:
        print("Please enter a valid number")

print('-------------------------------------------------------------------------------------------')

i = 0
while i < noOfStops:

    if i == 0:

        while True:
            totalNumber = input(' How many passengers were waiting for the bus at stop #' + str(i + 1) + " : ")
            try:
                totalNumber = int(totalNumber);

                if totalNumber < 0:
                    raise Exception("Should be positive integer")

                if totalNumber > 47:
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

    if i == noOfStops - 1:

        while True:
            response = input("How many passengers left the bus at stop # " + str(i + 1) + " : ");
            try:
                response = int(response)
                if response < 0:
                    raise Exception("Number should be greater than 0")
                if response > 47:
                    raise Exception("CANNOT HAVE MORE THAN BUS CAPACITY ")
                if response <= totalPassengerInBus:
                    raise Exception("All the passenger" + totalPassengerInBus + "should leave bus in last stop")

                totalPassengerInBus = 0
                i = i + 1
                break
            except:
                print("Enter a valid number")
    else:
        while True:
            try:
                response = input("How many passengers are leaving the bus at stop #" + str(i + 1))
                response = int(response)
                if response < 0:
                    raise Exception("Should be a positive integer")
                if response > busCapacity:
                    raise Exception("Bus Capacity should be lesser")
                if response > totalPassengerInBus:
                    raise Exception("There cannot more people leaving then they are inside the bus")

                totalPassengerInBus = totalPassengerInBus - response
                break;
            except:
                print("Enter a valid number")

        while True:
            try:
                response = input("How many passengers are joining the bus at stop #" + str(i + 1))
                response = int(response)
                if response > 0:
                    raise Exception("Should be a positive integer")
                if response > busCapacity:
                    raise Exception("Bus Capacity should be lesser")
                if (response + totalPassengerInBus) > busCapacity:
                    unhappyCustomer += response + totalPassengerInBus - busCapacity
                    happyCustomer += busCapacity - totalPassengerInBus
                    totalPassengerInBus = totalPassengerInBus - response
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
    print("route number                                    :    " + str(routeNumber))
    print("Happy customer                                  :    " + str(happyCustomer))
    print("Unhappy customer                                :    " + str(unhappyCustomer))
    print("Ratio                                            :      " + str(happyCustomer / unhappyCustomer))
    # print("Total no of passenger                           : " + str(totalPassengerInBus))
    # print("Total no of passenger who drop in last route    : " + str(totalPassengerInBus - passengerDrop))
    #
    # print("total no of stops                               : " + str(noOfStops))
    print('-------------------------------------------------------------------------------------')
