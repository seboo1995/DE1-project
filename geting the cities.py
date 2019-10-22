import pandas as pd

cities = pd.read_csv("cities_list.csv")

#creating list of cities but with duplicates
city_list = cities["City"]

city_list = city_list.tolist()
print(type(city_list))

city_list = list(dict.fromkeys(city_list))


print(len(city_list))
city_list.remove("Bergkamen")
city_list.remove("Berlin")
city_list.remove("Markersbach")
city_list.remove("Bexbach")
city_list.remove("Datteln")
city_list.remove("Dormagen")
city_list.remove("Elverlingsen")
city_list.remove("Ensdorf")
city_list.remove("Gundremmingen")
city_list.remove("Hamburg")
city_list.remove("Herdecke")
city_list.remove("Herne")
city_list.remove("Huckingen")
city_list.remove("Lingen")
city_list.remove("Ludwigshafen")
city_list.remove("Manheim")
city_list.remove("Munich")
city_list.remove("Wedel")
city_list.remove("Werne")

print(city_list)
print(len(city_list))




list_of_cities = ["Boxberg","Hamm-Uentrop","Lippendorf","Mainz","Spremberg","Knapsack","Rostock","Grevenbroich","Rostock","Grevenbroich",
"Bergheim","Goldisthal","Schkopau","Laufenburg","Gelsenkirchen","Vianden","Quierschied","Eschweiler","Hamm"]
print(list_of_cities)
print(len(list_of_cities))