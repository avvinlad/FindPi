# Estimate pi with given random value 

from random import uniform

def estimate_pi(n):
    num_circle = 0 
    pi = 0

    for _ in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        dist = x**2 + y**2
        
        if dist <= 1:
            num_circle += 1
    
    return (4 * (num_circle / n))
