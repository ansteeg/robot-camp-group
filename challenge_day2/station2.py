from datetime import datetime 

def solution_station_2(x):
    
    userdate = datetime.strptime(x, "%Y-%m-%d")
    userday = userdate.strftime("%A")
    japanese_days = {
        "Monday" : "月曜日",
        "Tuesday" : "火曜日",
        "Wednesday" : "水曜日",
        "Thursday" : "木曜日",
        "Friday" : "金曜日",
        "Saturday" : "土曜日",
        "Sunday" : "日曜日" 
        }
    return japanese_days[userday]

   




            
