from datetime import datetime

def solution_station_2(date_str):
    # Parse the input string to a date object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the weekday name
    weekday_name = date_obj.strftime('%A')
    
    return weekday_name