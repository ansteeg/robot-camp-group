import datetime

def station2(date_str):
    """
    Returns the day of the week in Japanese for a given date string (YYYY-MM-DD).
    """
    days_jp = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    # Monday = 0, Sunday = 6. Japanese week starts with Monday.
    return days_jp[date_obj.weekday()]


date_input = input("Enter a date (YYYY-MM-DD): ")
print("That day is:", station2(date_input))