import datetime

def solution_station_2(date_str: str) -> str:
    """
    Return the weekday in Japanese for a date string 'YYYY-MM-DD'.
    (例: '2025-09-02' -> '火曜日')
    """
    days_jp = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except (TypeError, ValueError):
        
        return "?"
    return days_jp[date_obj.weekday()]
