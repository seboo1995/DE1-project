import pandas as pd
import numpy as np
data = pd.read_csv("outages.csv",encoding="latin1")
print(data)
print(data["Month"])

months = list(dict.fromkeys(data["Month"]))
print(months)

data['Month'] = np.select(
    [
        data["Month"] == "január",
        data["Month"] == "február",
        data["Month"] == "március",
        data["Month"] == "április",
        data["Month"] == "május",
        data["Month"] == "június",
        data["Month"] == "július",
        data["Month"] == "augusztus",
        data["Month"] == "szeptember",
        data["Month"] == "október",
        data["Month"] == "november",
        data["Month"] == "december"




    ], 
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",




    ], 
    default='Unknown'
)

print(data["Month"])

data.to_csv(r"/home/sebair/Desktop/withCorrectMonths.csv")