def are_both_primes(a,b): 
    def is_prime(n):
        if n < 2 :
            return False 
        for i in range (2,int(n**0.5) +1 ):
            if n % i == 0: 
                return False 
        return True 
        
    return is_prime(a) and is_prime(b)
    
print(are_both_primes(95, 34307))
