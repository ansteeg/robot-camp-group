from datetime import datetime, timedelta

def solution_station_2(date2):
    dt2 = datetime.strptime(date2, "%Y-%m-%d")
    japanese_weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    return japanese_weekdays[dt2.weekday()]




