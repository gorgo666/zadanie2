import json
from math import sin, cos, sqrt, atan2, radians
# importowanie pliku json
with open('Zamu9HSa.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


print("Witaj użytkowniku! W okolicy znajduje się", len(data["data"]), "miejsc, które warto zwiedzić")
R = 6373

try:
    actualLatitude = float(input("wpisz swoją szerokość geograficzną: "))
    if -90 < actualLatitude > 90:
        print("użyj szerokości od -90.000000 do 90.000000")
    actualLongitude = float(input("wpisz długość geograficzną: "))
    if 0 < actualLongitude > 180:
        print("użyjdługośi pomiędzy 0 a 180.000000")
except:
    print("wprowadż poprawne dane, to muszą być cyfry")

actualLatitude = radians(actualLatitude)
actualLongitude = radians(actualLongitude)

i = 1

for x in data["data"]: 
    latitude = radians(x["location"]["latitude"])
    longitude = radians(x["location"]["longitude"])
    
    dlat = actualLatitude - latitude
    dlon = actualLongitude - longitude

    a = sin(dlat / 2)**2 + cos(actualLatitude) * cos(latitude) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    if distance <= 1:
        print( i , "." , x["name"], "-", round(distance * 1000, 2) , "metrów od Ciebie")
        i = i + 1
