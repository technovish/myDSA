def hotel_cost(nights):
    print (140*nights)

def plane_ride_cost(city):
    if (city == "Charlotte"):
        print("183")

    elif (city == "Tampa"):
        print("220")

    elif (city == "Pittsburgh"):
        print("222")

    elif (city == "Los Angeles"):
        print("475")
    else:
        return "Invalid City"


def rental_car_cost(days):
    if (days < 7 and days >= 3):
        print(40 * days - 20)
    elif (days < 7 and not days >= 3):
       print(40 * days)
    elif (days >= 7):
        print(40 * days - 50)


def trip_cost(city, days):
    rental_car_cost(days)
    hotel_cost(days-1)
    plane_ride_cost(city)


trip_cost("Tampa",3)