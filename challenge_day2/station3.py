def solution_station_3(a): 
    def is_prime(n):
        if n < 2 :
            return False 
        for i in range (2,int(n**0.5) +1 ):
            if n % i == 0: 
                return False 
        return True 
        
    return is_prime(a)
    
print(solution_station_3(34307))
print(solution_station_3(95))
