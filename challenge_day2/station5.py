def solution_station_5(student):
    team = None
    
    lt_1 = ["Tiara","Ebony","Nandini","Nathan","Ben","Muni","Lula","Tobit","Klementyna","Ainas","Yasmin","Julia","Luliia","Markus","Mufang","Oumaima", 'Zoë',"Yurui","Christopher","Yuvraj"]
    lt_2 = ["Huy Bao", "Iris", "Katharina", "Minseo", "Sade", "Alex", "Arwen", "Rajko", "Sylwia", "Zeno", "Christina", "Helen", "Mark", "Mats", "Vadim", "David", "Lora", "Quinn", "Tarling"]
    lt_3 = ["Elizabeth", "Gabriel", "Jakub", "Luc", "Soelie", "Aleksandra", "Arnav", "Donna", "Milan", "Rongze", "Cris", "Jingqi", "Oliver", "Vaayu", "Yusef", "Afua", "Anna", "Daniel", "Nataly", "Rafael"]
    lt_4 = ["Jeremy","Krishiv", 'Neel', 'Yujie', 'Yutong', 'An', 'Heer', 'Paige', 'Samir', 'Amalia', 'Douwe', 'Illya', 'Maria', 'Rakin', 'Lara', 'Lucas', 'Michelle', 'Oliwia', 'Tom']

    if student in lt_1:
        team = 1
    elif student in lt_2:
        team = 2
    elif student in lt_3:
        team = 3
    elif student in lt_4:
        team = 4
    else:
        team = 0

    teams = int(team) 
    
    return teams


##solution_station_5("Jeremy")