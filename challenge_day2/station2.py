import datetime

def solution_station_2(input_value: str) -> str:
    """
    This function converts a date string to the day of the week in Japanese.
    """
    days_jp = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    
    try:
        # Accommodate for potential typos in date format
        cleaned_date_str = input_value.replace(' ', '').replace('O', '0') # Common OCR errors
        if len(cleaned_date_str) == 9 and cleaned_date_str[4] != '-': # e.g., 202403-24
            cleaned_date_str = cleaned_date_str[:4] + '-' + cleaned_date_str[4:6] + '-' + cleaned_date_str[7:]

        date_obj = datetime.datetime.strptime(cleaned_date_str, '%Y-%m-%d')
        return days_jp[date_obj.weekday()]
    except (ValueError, IndexError):
        # Return a default or handle the error as appropriate for the challenge
        return ""