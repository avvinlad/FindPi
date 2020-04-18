from estimate_pi import estimate_pi

def main():
    total = int(input("Number of Data Points (0 to exit): "))

    while (total != 0):
        print("Estimate of Pi: {:f}".format(estimate_pi(total)))
        total = int(input("Number of Data Points (0 to exit): "))


if __name__ == "__main__":
    main()