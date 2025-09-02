def solution_station_5(student_name):
    """
    Find the learning team number by student name.
    
    Inputs:
        student_name (str): The name of the student.
    
    Outputs:
        The learning team number(int): Returns -1 if the student is not found.
    """
    learningTeams = {
    1: ["Daeho", "David", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", 
        "Riya", "Vassil", "Twan", "Ester", "Karolina", "Lena", "Margarita", 
        "Anna", "Kien", "Klaudia", "Maliah", "Todd"],

    2: ["Oumaima", "Mathilde", "Marie", "Anita", "Ziyan", "Bernardo", 
        "Eleanor", "Lorijn", "Maria", "Younes", "Yvan", "Henning", 
        "Liangyu", "Maciej", "Toprak", "Chris", "GengXin", "Mingze", "Phoebe"],

    3: ["Betija", "Haider", "Kacper", "Sophie", "Amir", "Baltasar", "Isar", 
        "Jelle", "Nicolas", "David", "Ipek", "Juan", "Marfa", "Maria", 
        "Alissa", "Leopoldo", "Mies", "Jiaying", "Kaixin", "Mai", "Sem", "Tibbe", "Madeleine"],

    4: ["Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna", "Ekaterina", 
        "Thessa", "Tongfei", "Yang", "Benedikt", "Jan", "Nadee", "Osjah", 
        "Tim", "Eliana", "Joana", "Peilin", "Pija", "Wenhao"],

    5: ["Afua", "Cristina", "Greta", "Jace", "Laura", "Anna", "Bassant", 
        "Ivan", "Juriaan", "Kiavash"],

    6: ["Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", 
        "Olesya", "Sophie", "Tom"]
}
    for team_id, members in learningTeams.items():
        if student_name in members:
            return team_id
    return -1
