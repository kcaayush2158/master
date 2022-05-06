import os

count = 0;
fileLength = 0;
strippedLine = 0;

errorMessage = "Error reading data. \n Please ensure each line of routes.txt contains a route  number, followed by a comma, \n followed by a happy ratio  \n and that no route  is repeated throughout the file"
routeArray = []
disc = []


def sort_route_data():
    print("shorting")

# function that reads the routing text
def read_route_data(fileName):
    if os.path.getsize(fileName) == 0:
        raise Exception(errorMessage)

    with open(fileName, 'r') as file:
        content = file.readlines()

        # stores the line length from a file
        fileLength = content.__len__()

        for line in content:
            # returns a copy of the string
            strippedLine = line.strip()
            if strippedLine == "":
                raise Exception(errorMessage);
            # splits the text
            routeArray = strippedLine.split(",")

            try:
                # stores a route number and  the ratio number of happy and unhappy numbers

                busRoute = {'route_number': float(routeArray[0]), "happy_ratio ": float(routeArray[1])}
                disc.append(busRoute)

                print(float(routeArray[0]))
            except ValueError:
                raise Exception(errorMessage)
    file.close()


while True:
    try:
        addBus = input("How many routes can have an extra bus? ")
        n = int(addBus);
        if n < 0:
            print("Invalid value. Please enter a non-negative integer")
        else:
            read_route_data("routes.txt")
            break
    except ValueError:
        raise Exception(errorMessage)

# show error message
if n < fileLength:
    raise Exception(errorMessage)
else:

    routeNumber = input("Enter the route number :")
    try:
        routeNumber = int(routeNumber);
        for route in disc:
            if route['route_number'] != n:
                raise Exception("This route is not available")
            else:
                print("route available")
                break

    except ValueError:
        print("Please enter a valid number")



