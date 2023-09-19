import requests
from datetime import datetime, timedelta

days_look_ahead = 3
days_look_ahead_week = 8

tomorrow = datetime.now().date() + timedelta(days=days_look_ahead)
date = tomorrow.strftime("%m/%d/%Y")

next_week = tomorrow = datetime.now().date() + timedelta(days=days_look_ahead_week)
next_week_date = next_week.strftime("%m/%d/%Y")

url = f"https://spor.kadikoy.bel.tr/Ajax/GetAreaReservationList.ashx?facilityId=3&AreaId=8&firstDayOfWeekLong={date}"
url_next_week = f"https://spor.kadikoy.bel.tr/Ajax/GetAreaReservationList.ashx?facilityId=3&AreaId=8&firstDayOfWeekLong={next_week_date}"

response = requests.get(url)
response_next_week = requests.get(url_next_week)

hour_eight = "20:00/21:00"
hour_nine = "21:00/22:00"
hour_ten = "22:00/23:00"

for listing in response.json()["programs"]:

    # statu 0 is reserved, 1 is available
    if listing["statu"] == 1:
        if(hour_eight in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])
        elif (hour_nine in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])
        elif (hour_ten in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])

for listing in response_next_week.json()["programs"]:

    # statu 0 is reserved, 1 is available
    if listing["statu"] == 1:
        if(hour_eight in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])
        elif (hour_nine in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])
        elif (hour_ten in listing["hourData"]):
            print(listing["programDateFormatted"], listing["hourData"])
        