import requests
from datetime import datetime, timedelta

def get_week_days(delta=0):
    today = datetime.today() + timedelta(days=delta)

    days_ahead = 0 - today.weekday() 

    if days_ahead < 0:  
        days_ahead += 7  # Get next Monday

    first_day_this_week = today + timedelta(days=days_ahead)


    return first_day_this_week

pages = []
hour_eight = "20:00/21:00"
hour_nine = "21:00/22:00"
hour_ten = "22:00/23:00"


for i in range(0, 4):
    tw = get_week_days(i*7)

    i_look_ahead = tw.strftime("%m/%d/%Y")

    url = f"https://spor.kadikoy.bel.tr/Ajax/GetAreaReservationList.ashx?facilityId=3&AreaId=8&firstDayOfWeekLong={i_look_ahead}"
    response = requests.get(url)

    pages.append(response.json())


slots =set() 

for page in pages:
    for listing in page["programs"]:
        # statu 0 is reserved, 1 is available
        if listing["statu"] == 1:
            if hour_ten in listing["hourData"] or hour_nine in listing["hourData"] or hour_eight in listing["hourData"]:
                slots.add(listing["programDateFormatted"] + " " + listing["hourData"])

for empty_rez in slots:
    print(empty_rez)
