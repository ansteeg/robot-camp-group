import datetime

# Japanese weekdays
japanese_weekdays = {
    0: "月曜日",  # Monday
    1: "火曜日",  # Tuesday
    2: "水曜日",  # Wednesday
    3: "木曜日",  # Thursday
    4: "金曜日",  # Friday
    5: "土曜日",  # Saturday
    6: "日曜日",  # Sunday
}

def get_japanese_weekdays(date_list):
    results = {}
    for date_str in date_list:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        weekday_num = date_obj.weekday()
        results[date_str] = japanese_weekdays[weekday_num]
    return results

# Example usage
dates = ["2024-01-20", "2024-08-28", "2024-04-23"]
weekdays = get_japanese_weekdays(dates)

for d, wd in weekdays.items():
    print(f"{d} → {wd}")
