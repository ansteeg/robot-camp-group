<<<<<<< HEAD
# Madeleine and Kacper
import datetime


def solution_station_1(date_str):
    # Parse the date string (expects YYYY-MM-DD)
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get weekday (0 = Monday, 6 = Sunday)
    weekday_index = date_obj.weekday()
    
    # English -> Japanese mapping
    days_jp = {
        0: "月曜日 (Getsuyōbi)",   # Monday
        1: "火曜日 (Kayōbi)",     # Tuesday
        2: "水曜日 (Suiyōbi)",    # Wednesday
        3: "木曜日 (Mokuyōbi)",   # Thursday
        4: "金曜日 (Kin’yōbi)",   # Friday
        5: "土曜日 (Doyōbi)",     # Saturday
        6: "日曜日 (Nichiyōbi)"   # Sunday
    }
    
    # weekday() gives 0–6, but with Monday=0 … Sunday=6
    japanese_day = days_jp[weekday_index]
    
    return japanese_day

# Example usage
date_input = "2023-02-26"
print(f"{date_input} is {solution_station_1(date_input)}")
=======
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
>>>>>>> a12f914dc4bb7fd7b2bfecfefa3352ae29f469e0
