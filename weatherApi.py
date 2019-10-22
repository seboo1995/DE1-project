from wwo_hist import retrieve_hist_data
import os
os.chdir("/home/sebair/Desktop/projectDE1API")






list_of_cities = ["Boxberg","Hamm-Uentrop","Lippendorf","Mainz","Spremberg","Knapsack","Rostock","Grevenbroich","Rostock","Grevenbroich",
"Bergheim","Goldisthal","Schkopau","Laufenburg","Gelsenkirchen","Vianden","Quierschied","Eschweiler","Hamm"]






frequency  = 24
start_date = "01-JAN-2018"
end_date = "01-JAN-2019"
api_key = "0793d6726ce7417cab1204259191410"
location_list = list_of_cities
hist_weather_data = retrieve_hist_data(api_key,location_list,start_date,end_date,frequency,location_label=False,export_csv=True,store_df=True
)
