import datetime


def solution_station_2(date_str: str) -> str:
	# Return the weekday in Japanese for the given YYYY-MM-DD date string
	# Monday=0 ... Sunday=6 mapping
	japanese_weekdays = {
		0: "月曜日",
		1: "火曜日",
		2: "水曜日",
		3: "木曜日",
		4: "金曜日",
		5: "土曜日",
		6: "日曜日",
	}
	date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
	weekday_num = date_obj.weekday()
	return japanese_weekdays[weekday_num]


