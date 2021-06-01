from is_even import is_even as ie

def main(number):
    if ie.is_odd(number) == True:
        print("Your number is odd!")
    else:
        print("You number is not odd.")


if __name__ == "__main__":
    main(2)
