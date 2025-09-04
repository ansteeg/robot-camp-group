#Madeleine and Kacper
import datetime
def solution_station_2(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday_index = date_obj.weekday()
    days_jp = {
        0: "月曜日",   # Monday
        1: "火曜日",     # Tuesday
        2: "水曜日",    # Wednesday
        3: "木曜日",   # Thursday
        4: "金曜日",   # Friday
        5: "土曜日",     # Saturday
        6: "日曜日"   # Sunday
    }

    return days_jp[weekday_index]

#print(solution_station_2("2023-06-10"))
#print(solution_station_2("2023-09-25"))
