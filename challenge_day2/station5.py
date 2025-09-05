def solution_station_5(name: str) -> int:

    learning_teams = {
        # LT 1
        "daeho": 1, "david": 1, "kaisa": 1, "oliver": 1, "sara": 1, "dan": 1, 
        "ivar": 1, "lotte": 1, "riya": 1, "vassil": 1, "twan": 1, "ester": 1, 
        "karolina": 1, "lena": 1, "margarita": 1, "anna": 1, "kien": 1, 
        "klaudia": 1, "maliah": 1, "todd": 1,
        
        # LT 2
        "oumaima": 2, "mathilde": 2, "marie": 2, "anita": 2, "ziyan": 2, 
        "bernardo": 2, "eleanor": 2, "lorijn": 2, "maria": 2, "younes": 2, 
        "yvan": 2, "henning": 2, "liangyu": 2, "maciej": 2, "toprak": 2, 
        "chris": 2, "gengxin": 2, "mingze": 2, "phoebe": 2,
        
        # LT 3
        "betija": 3, "haider": 3, "kacper": 3, "sophie": 3, "amir": 3, 
        "baltasar": 3, "isar": 3, "jelle": 3, "nicolas": 3, "ipek": 3, 
        "juan": 3, "marfa": 3, "alissa": 3, "leopoldo": 3, "mies": 3, 
        "jiaying": 3, "kaixin": 3, "mai": 3, "sem": 3, "tibbe": 3,
        "david": 3, "maria": 3,
        
        # LT 4
        "justus": 4, "julia": 4, "philip": 4, "uli": 4, "vanessa": 4, 
        "ekaterina": 4, "thessa": 4, "tongfei": 4, "yang": 4, "benedikt": 4, 
        "jan": 4, "nadee": 4, "osjah": 4, "tim": 4, "eliana": 4, "joana": 4, 
        "peilin": 4, "pija": 4, "wenhao": 4,
        "anna": 4,
        
        # LT 5
        "afua": 5, "cristina": 5, "greta": 5, "jace": 5, "laura": 5, 
        "bassant": 5, "ivan": 5, "juriaan": 5, "kiavash": 5,
        "anna": 5,

        # LT 6
        "keitaro": 6, "nohemi": 6, "norina": 6, "yifan": 6, "yinan": 6, 
        "luo": 6, "nikola": 6, "olesya": 6, "tom": 6,
        "sophie": 6,
    }
    
    return learning_teams.get(name.lower(), 0)

if __name__ == '__main__':
    print("--- Testing specific names from the list ---")
    print(f"Kien -> {solution_station_5('Kien')}")           # Expected: 1
    print(f"Phoebe -> {solution_station_5('Phoebe')}")       # Expected: 2
    print(f"Leopoldo -> {solution_station_5('Leopoldo')}")   # Expected: 3
    print(f"Nadee -> {solution_station_5('Nadee')}")         # Expected: 4
    print(f"Juriaan -> {solution_station_5('Juriaan')}")     # Expected: 5
    print(f"Tom -> {solution_station_5('Tom')}")             # Expected: 6
    
    print("\n--- Testing names that appear in multiple lists ---")
    print(f"Maria -> {solution_station_5('Maria')}")         # Expected: 3
    print(f"Sophie -> {solution_station_5('Sophie')}")       # Expected: 6
    print(f"Anna -> {solution_station_5('Anna')}")           # Expected: 5
    
    print("\n--- Testing with an unknown name ---")
    print(f"Roland -> {solution_station_5('Roland')}")       # Expected: 0