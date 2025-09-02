
def solution_station_5(name):


    LT1 = ["Daeho", "David", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", 
           "Riya", "Vassil", "Twan", "Ester", "Karolina", "Lena", "Margarita", 
           "Anna", "Kien", "Klaudia", "Maliah", "Todd"]

    LT2 = ["Oumaima", "Mathilde", "Marie", "Anita", "Ziyan", "Bernardo", 
           "Eleanor", "Lorijn", "Maria", "Younes", "Yvan", "Henning", "Liangyu", 
           "Maciej", "Toprak", "Chris", "GengXin", "Mingze", "Phoebe"]

    LT3 = ["Betija", "Haider", "Kacper", "Sophie", "Amir", "Baltasar", "Isar", 
           "Jelle", "Nicolas", "David", "Ipek", "Juan", "Marfa", "Maria", "Alissa", 
           "Leopoldo", "Mies", "Jiaying", "Kaixin", "Mai", "Sem", "David C", "Tibbe"]

    LT4 = ["Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna", "Ekaterina", 
           "Thessa", "Tongfei", "Yang", "Benedikt", "Jan", "Nadee", "Osjah", "Tim", 
           "Eliana", "Joana", "Peilin", "Pija", "Wenhao"]

    LT5 = ["Afua", "Cristina", "Greta", "Jace", "Laura", "Anna", "Bassant", 
           "Ivan", "Juriaan", "Kiavash"]

    LT6 = ["Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", 
           "Olesya", "Sophie", "Tom"]

    
    teams = {
        1: LT1,
        2: LT2,
        3: LT3,
        4: LT4,
        5: LT5,
        6: LT6
    }

    
    for number, members in teams.items():
        if name in members:
            return number

    return None  
