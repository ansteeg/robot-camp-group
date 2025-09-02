def is_this_prime(a): 
    def is_prime(n):
        if n < 2 :
            return False 
        for i in range (2,int(n**0.5) +1 ):
            if n % i == 0: 
                return False 
        return True 
        
    return is_prime(a)
    
print(is_this_prime(34307))
print(is_this_prime(95))
