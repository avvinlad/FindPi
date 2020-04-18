# Estimate pi with given random value 
import random

def main():
    total = int(input("Number of Data Points (0 to exit): "))
    while (total != 0):
        print("Estimate of Pi: {:f}".format(estimate_pi(total)))
        total = int(input("Number of Data Points (0 to exit): "))


def estimate_pi(n):
    num_circle = 0
    pi = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        dist = x**2 + y**2
        
        if dist <= 1:
            num_circle += 1
    
    return (4 * (num_circle / n))


if __name__ == "__main__":
    main()